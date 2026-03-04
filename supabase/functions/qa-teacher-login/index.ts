import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const ALLOWED_ORIGINS = new Set([
  "https://kirkmanamos.github.io",
  "http://localhost:4173",
  "http://localhost:5500",
]);

const TOKEN_TTL_SECONDS = 60 * 60 * 8;

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

async function sha256Hex(value: string) {
  const bytes = new TextEncoder().encode(value);
  const digest = await crypto.subtle.digest("SHA-256", bytes);
  return Array.from(new Uint8Array(digest))
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
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

async function createTeacherToken(payload: Record<string, unknown>, secret: string) {
  const header = { alg: "HS256", typ: "JWT" };
  const encodedHeader = toBase64Url(new TextEncoder().encode(JSON.stringify(header)));
  const encodedPayload = toBase64Url(new TextEncoder().encode(JSON.stringify(payload)));
  const data = `${encodedHeader}.${encodedPayload}`;
  const signature = await hmacSign(data, secret);
  return `${data}.${signature}`;
}

function isTokenShapeValid(value: string) {
  const parts = value.split(".");
  if (parts.length !== 3) return false;
  try {
    fromBase64Url(parts[0]);
    fromBase64Url(parts[1]);
    return true;
  } catch (_) {
    return false;
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
  const sessionCode = typeof body?.sessionCode === "string" ? body.sessionCode.trim() : "";
  const passcode = typeof body?.passcode === "string" ? body.passcode : "";
  if (!sessionCode || !passcode) {
    return jsonResponse(origin, 400, { ok: false, error: "sessionCode and passcode are required." });
  }

  const admin = createClient(supabaseUrl, serviceRoleKey, {
    auth: { persistSession: false },
  });

  const { data: session, error: sessionError } = await admin
    .from("qa_sessions")
    .select("session_code, deck_slug, teacher_passcode_hash, is_active, expires_at")
    .eq("session_code", sessionCode)
    .maybeSingle();

  if (sessionError || !session) {
    return jsonResponse(origin, 404, { ok: false, error: "Session not found." });
  }
  if (!session.is_active) {
    return jsonResponse(origin, 403, { ok: false, error: "Session is inactive." });
  }
  if (session.expires_at && new Date(session.expires_at).getTime() <= Date.now()) {
    return jsonResponse(origin, 403, { ok: false, error: "Session has expired." });
  }

  const inputHash = await sha256Hex(passcode);
  if (inputHash !== session.teacher_passcode_hash) {
    return jsonResponse(origin, 401, { ok: false, error: "Invalid passcode." });
  }

  const exp = Math.floor(Date.now() / 1000) + TOKEN_TTL_SECONDS;
  const expiresAt = new Date(exp * 1000).toISOString();
  const token = await createTeacherToken(
    {
      sessionCode: session.session_code,
      deckSlug: session.deck_slug,
      exp,
    },
    jwtSecret,
  );

  if (!isTokenShapeValid(token)) {
    return jsonResponse(origin, 500, { ok: false, error: "Token generation failed." });
  }

  return jsonResponse(origin, 200, { ok: true, token, expiresAt });
});
