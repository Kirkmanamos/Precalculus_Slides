-- Student Q&A pilot schema for 5.1 fundamental identities.
-- Run this in Supabase SQL editor.

create extension if not exists pgcrypto;

create table if not exists public.qa_sessions (
  session_code text primary key,
  deck_slug text not null,
  teacher_passcode_hash text not null,
  is_active boolean not null default true,
  created_at timestamptz not null default now(),
  expires_at timestamptz
);

create table if not exists public.qa_questions (
  id uuid primary key default gen_random_uuid(),
  session_code text not null references public.qa_sessions(session_code) on delete cascade,
  deck_slug text not null,
  question_text text not null check (char_length(question_text) between 1 and 280),
  slide_id text,
  slide_index integer,
  slide_title text,
  status text not null default 'pending' check (status in ('pending', 'approved', 'hidden')),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  approved_at timestamptz
);

alter table public.qa_questions
  add column if not exists slide_id text,
  add column if not exists slide_index integer,
  add column if not exists slide_title text;

create table if not exists public.qa_rate_limit (
  id bigint generated always as identity primary key,
  session_code text not null references public.qa_sessions(session_code) on delete cascade,
  ip_hash text not null,
  submitted_at timestamptz not null default now()
);

create index if not exists qa_questions_session_deck_created_idx
  on public.qa_questions (session_code, deck_slug, created_at desc);

create index if not exists qa_questions_session_deck_status_idx
  on public.qa_questions (session_code, deck_slug, status);

create index if not exists qa_rate_limit_session_ip_time_idx
  on public.qa_rate_limit (session_code, ip_hash, submitted_at desc);

create or replace function public.set_qa_questions_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

drop trigger if exists trg_set_qa_questions_updated_at on public.qa_questions;
create trigger trg_set_qa_questions_updated_at
before update on public.qa_questions
for each row
execute function public.set_qa_questions_updated_at();

alter table public.qa_sessions enable row level security;
alter table public.qa_questions enable row level security;
alter table public.qa_rate_limit enable row level security;

drop policy if exists qa_questions_read_approved on public.qa_questions;
create policy qa_questions_read_approved
on public.qa_questions
for select
to anon
using (status = 'approved');

grant select on public.qa_questions to anon;

revoke all on public.qa_sessions from anon, authenticated;
revoke all on public.qa_rate_limit from anon, authenticated;
revoke insert, update, delete on public.qa_questions from anon, authenticated;
