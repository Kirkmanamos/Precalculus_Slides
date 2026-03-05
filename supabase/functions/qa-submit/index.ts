import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const ALLOWED_ORIGINS = new Set([
  "https://kirkmanamos.github.io",
  "http://localhost:4173",
  "http://localhost:5500",
  "http://localhost:8000",
  "http://127.0.0.1:8000",
]);

const MAX_QUESTION_LENGTH = 280;
const MAX_SLIDE_TITLE_LENGTH = 160;
const RATE_LIMIT_WINDOW_MS = 60_000;
const RATE_LIMIT_MAX_SUBMITS = 3;

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

function getClientIp(req: Request) {
  const forwarded = req.headers.get("x-forwarded-for");
  if (forwarded) return forwarded.split(",")[0].trim();
  return req.headers.get("x-real-ip") || "unknown";
}

async function sha256Hex(value: string) {
  const bytes = new TextEncoder().encode(value);
  const digest = await crypto.subtle.digest("SHA-256", bytes);
  return Array.from(new Uint8Array(digest))
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
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

  const supabaseUrl = Deno.env.get("QA_SUPABASE_URL") || Deno.env.get("SUPABASE_URL");
  const serviceRoleKey = Deno.env.get("QA_SUPABASE_SERVICE_ROLE_KEY") || Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");
  if (!supabaseUrl || !serviceRoleKey) {
    return jsonResponse(origin, 500, { ok: false, error: "Server is missing Supabase env vars." });
  }

  const body = await req.json().catch(() => null);
  const sessionCode = typeof body?.sessionCode === "string" ? body.sessionCode.trim() : "";
  const deckSlug = typeof body?.deckSlug === "string" ? body.deckSlug.trim() : "";
  const questionText = typeof body?.questionText === "string" ? body.questionText.trim() : "";
  const slideId = typeof body?.slideId === "string" ? body.slideId.trim() : "";
  const slideTitle = typeof body?.slideTitle === "string" ? body.slideTitle.trim() : "";
  const rawSlideIndex = body?.slideIndex;
  const slideIndex = Number.isInteger(rawSlideIndex) && rawSlideIndex >= 0 ? rawSlideIndex : null;

  if (!sessionCode || !deckSlug || !questionText) {
    return jsonResponse(origin, 400, { ok: false, error: "sessionCode, deckSlug, and questionText are required." });
  }
  if (questionText.length > MAX_QUESTION_LENGTH) {
    return jsonResponse(origin, 400, { ok: false, error: `questionText must be ${MAX_QUESTION_LENGTH} characters or fewer.` });
  }
  if (slideTitle.length > MAX_SLIDE_TITLE_LENGTH) {
    return jsonResponse(origin, 400, { ok: false, error: `slideTitle must be ${MAX_SLIDE_TITLE_LENGTH} characters or fewer.` });
  }

  const admin = createClient(supabaseUrl, serviceRoleKey, {
    auth: { persistSession: false },
  });

  const { data: session, error: sessionError } = await admin
    .from("qa_sessions")
    .select("session_code, deck_slug, is_active, expires_at")
    .eq("session_code", sessionCode)
    .maybeSingle();

  if (sessionError || !session) {
    return jsonResponse(origin, 404, { ok: false, error: "Session not found." });
  }
  if (!session.is_active) {
    return jsonResponse(origin, 403, { ok: false, error: "Session is inactive." });
  }
  if (session.deck_slug !== deckSlug) {
    return jsonResponse(origin, 400, { ok: false, error: "Session code does not match this deck." });
  }
  if (session.expires_at && new Date(session.expires_at).getTime() <= Date.now()) {
    return jsonResponse(origin, 403, { ok: false, error: "Session has expired." });
  }

  const clientIp = getClientIp(req);
  const userAgent = req.headers.get("user-agent") || "";
  const ipHash = await sha256Hex(`${clientIp}|${userAgent}`);
  const since = new Date(Date.now() - RATE_LIMIT_WINDOW_MS).toISOString();

  const { count, error: rateError } = await admin
    .from("qa_rate_limit")
    .select("id", { count: "exact", head: true })
    .eq("session_code", sessionCode)
    .eq("ip_hash", ipHash)
    .gt("submitted_at", since);

  if (rateError) {
    return jsonResponse(origin, 500, { ok: false, error: "Rate-limit lookup failed." });
  }
  if ((count || 0) >= RATE_LIMIT_MAX_SUBMITS) {
    return jsonResponse(origin, 429, { ok: false, error: "Rate limit reached. Try again in a minute." });
  }

  const { error: rlInsertError } = await admin.from("qa_rate_limit").insert({
    session_code: sessionCode,
    ip_hash: ipHash,
  });
  if (rlInsertError) {
    return jsonResponse(origin, 500, { ok: false, error: "Rate-limit write failed." });
  }

  const { data: created, error: insertError } = await admin
    .from("qa_questions")
    .insert({
      session_code: sessionCode,
      deck_slug: deckSlug,
      question_text: questionText,
      slide_id: slideId || null,
      slide_index: slideIndex,
      slide_title: slideTitle || null,
      status: "pending",
    })
    .select("id")
    .single();

  if (insertError || !created) {
    return jsonResponse(origin, 500, { ok: false, error: "Failed to create question." });
  }

  return jsonResponse(origin, 200, { ok: true, questionId: created.id });
});
