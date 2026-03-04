import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const ALLOWED_ORIGINS = new Set([
  "https://kirkmanamos.github.io",
  "http://localhost:4173",
  "http://localhost:5500",
]);

const VALID_ACTIONS = new Set(["approve", "reopen", "hide", "clear_hidden", "clear_all", "list"]);

function corsHeaders(origin: string | null) {
  const allowOrigin = origin && ALLOWED_ORIGINS.has(origin) ? origin : "null";
  return {
    "Access-Control-Allow-Origin": allowOrigin,
    "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
  };
}

function jsonResponse(origin: string | null, status: number, body: Record<string, unknown>) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      ...corsHeaders(origin),
      "Content-Type": "application/json",
    },
  });
}

function toBase64Url(input: Uint8Array) {
  const str = String.fromCharCode(...input);
  return btoa(str).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
}

function fromBase64Url(input: string) {
  const base64 = input.replace(/-/g, "+").replace(/_/g, "/");
  const padded = base64 + "=".repeat((4 - (base64.length % 4)) % 4);
  return atob(padded);
}

async function hmacSign(data: string, secret: string) {
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const sig = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(data));
  return toBase64Url(new Uint8Array(sig));
}

async function verifyTeacherToken(token: string, secret: string) {
  const parts = token.split(".");
  if (parts.length !== 3) return { ok: false, error: "Malformed token." } as const;

  const [headerPart, payloadPart, signaturePart] = parts;
  const expected = await hmacSign(`${headerPart}.${payloadPart}`, secret);
  if (expected !== signaturePart) return { ok: false, error: "Invalid token signature." } as const;

  try {
    const payloadJson = fromBase64Url(payloadPart);
    const payload = JSON.parse(payloadJson) as { sessionCode?: string; deckSlug?: string; exp?: number };
    if (!payload.sessionCode || !payload.deckSlug || !payload.exp) {
      return { ok: false, error: "Token payload is missing required fields." } as const;
    }
    if (payload.exp <= Math.floor(Date.now() / 1000)) {
      return { ok: false, error: "Token has expired." } as const;
    }
    return { ok: true, payload } as const;
  } catch (_) {
    return { ok: false, error: "Token payload decode failed." } as const;
  }
}

Deno.serve(async (req) => {
  const origin = req.headers.get("origin");

  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: corsHeaders(origin) });
  }

  if (!origin || !ALLOWED_ORIGINS.has(origin)) {
    return jsonResponse(origin, 403, { ok: false, error: "Origin not allowed." });
  }

  if (req.method !== "POST") {
    return jsonResponse(origin, 405, { ok: false, error: "Method not allowed." });
  }

  const supabaseUrl = Deno.env.get("SUPABASE_URL");
  const serviceRoleKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");
  const jwtSecret = Deno.env.get("QA_TEACHER_JWT_SECRET");
  if (!supabaseUrl || !serviceRoleKey || !jwtSecret) {
    return jsonResponse(origin, 500, { ok: false, error: "Server is missing required env vars." });
  }

  const body = await req.json().catch(() => null);
  const token = typeof body?.token === "string" ? body.token : "";
  const action = typeof body?.action === "string" ? body.action : "";
  const questionId = typeof body?.questionId === "string" ? body.questionId : "";
  const sessionCode = typeof body?.sessionCode === "string" ? body.sessionCode.trim() : "";
  const deckSlug = typeof body?.deckSlug === "string" ? body.deckSlug.trim() : "";

  if (!token || !action || !sessionCode || !deckSlug) {
    return jsonResponse(origin, 400, { ok: false, error: "token, action, sessionCode, and deckSlug are required." });
  }
  if (!VALID_ACTIONS.has(action)) {
    return jsonResponse(origin, 400, { ok: false, error: "Unsupported action." });
  }
  if (["approve", "reopen", "hide"].includes(action) && !questionId) {
    return jsonResponse(origin, 400, { ok: false, error: "questionId is required for this action." });
  }

  const verified = await verifyTeacherToken(token, jwtSecret);
  if (!verified.ok) {
    return jsonResponse(origin, 401, { ok: false, error: verified.error });
  }

  if (verified.payload.sessionCode !== sessionCode || verified.payload.deckSlug !== deckSlug) {
    return jsonResponse(origin, 403, { ok: false, error: "Token does not match this session/deck." });
  }

  const admin = createClient(supabaseUrl, serviceRoleKey, {
    auth: { persistSession: false },
  });

  if (action === "list") {
    const { data, error } = await admin
      .from("qa_questions")
      .select("id, session_code, deck_slug, question_text, status, created_at, updated_at, approved_at")
      .eq("session_code", sessionCode)
      .eq("deck_slug", deckSlug)
      .order("created_at", { ascending: false });

    if (error) {
      return jsonResponse(origin, 500, { ok: false, error: "Failed to load question list." });
    }
    return jsonResponse(origin, 200, { ok: true, questions: data || [] });
  }

  if (action === "approve") {
    const { error } = await admin
      .from("qa_questions")
      .update({ status: "approved", approved_at: new Date().toISOString() })
      .eq("id", questionId)
      .eq("session_code", sessionCode)
      .eq("deck_slug", deckSlug);
    if (error) return jsonResponse(origin, 500, { ok: false, error: "Failed to approve question." });
    return jsonResponse(origin, 200, { ok: true });
  }

  if (action === "reopen") {
    const { error } = await admin
      .from("qa_questions")
      .update({ status: "pending", approved_at: null })
      .eq("id", questionId)
      .eq("session_code", sessionCode)
      .eq("deck_slug", deckSlug);
    if (error) return jsonResponse(origin, 500, { ok: false, error: "Failed to reopen question." });
    return jsonResponse(origin, 200, { ok: true });
  }

  if (action === "hide") {
    const { error } = await admin
      .from("qa_questions")
      .update({ status: "hidden" })
      .eq("id", questionId)
      .eq("session_code", sessionCode)
      .eq("deck_slug", deckSlug);
    if (error) return jsonResponse(origin, 500, { ok: false, error: "Failed to hide question." });
    return jsonResponse(origin, 200, { ok: true });
  }

  if (action === "clear_hidden") {
    const { error } = await admin
      .from("qa_questions")
      .delete()
      .eq("session_code", sessionCode)
      .eq("deck_slug", deckSlug)
      .eq("status", "hidden");
    if (error) return jsonResponse(origin, 500, { ok: false, error: "Failed to clear hidden questions." });
    return jsonResponse(origin, 200, { ok: true });
  }

  if (action === "clear_all") {
    const { error } = await admin
      .from("qa_questions")
      .delete()
      .eq("session_code", sessionCode)
      .eq("deck_slug", deckSlug);
    if (error) return jsonResponse(origin, 500, { ok: false, error: "Failed to clear all questions." });
    return jsonResponse(origin, 200, { ok: true });
  }

  return jsonResponse(origin, 400, { ok: false, error: "Action not implemented." });
});
