# Agent Handoff

Use this file when one AI assistant needs to pause work and let another assistant continue in this repository. Keep entries short, factual, and current. Append new handoffs above older ones; do not delete another agent's notes unless the task is complete and the note is no longer useful.

## Handoff Protocol

1. Read `AGENTS.md`, `CLAUDE.md`, `CONVENTIONS.md`, and any task-specific skill before editing.
2. Check `git status --short` before starting. Treat existing modified or untracked files as someone else's work unless you know you created them.
3. Work on a branch or worktree when possible. Avoid having two agents edit the same file at the same time.
4. Before pausing, add or update a handoff entry below.
5. Include exact checks run, even if they failed or were skipped.
6. Leave the next agent with one clear next action.

## Current Handoffs

### 2026-03-04 — Student Q&A Pilot (awaiting owner decision)

- **Agent**: Codex
- **Branch or worktree**: `codex/student-qa-pilot` (remote exists, never merged)
- **Task**: Add a live student Q&A system to the 5.1 deck, with Supabase backend for submission, moderation, and teacher login.
- **Files touched**:
  - `5.1-fundamental-identities.html` — student modal, teacher panel, realtime sync
  - `supabase/sql/qa_schema.sql`
  - `supabase/functions/qa-submit/index.ts`
  - `supabase/functions/qa-teacher-login/index.ts`
  - `supabase/functions/qa-moderate/index.ts`
  - `docs/student-qa-pilot-progress.md`
  - `docs/student-qa-supabase-setup.md`
- **Current state**: Complete and live-tested against hosted Supabase on 2026-03-05. Teacher unlock, student submission, realtime sync, rate limiting, and moderation all verified. Branch was never merged into `main`.
- **Checks run**:
  - Hosted Supabase deploy — passed
  - Teacher unlock flow — passed
  - Student submission — passed
- **Known issues or risks**: The `5.1-fundamental-identities.html` on this branch is based on an older version of that file and would need rebasing onto current `main` before merging. The branch also removed several files present on `main` (Unit 1 decks, SKILL_HTML.md, etc.) — do NOT merge directly; cherry-pick or rebase the Supabase files only.
- **Next action**: **Owner decides**: (A) abandon — close the PR, (B) continue — rebase onto main and integrate, or (C) extract — cherry-pick only the `supabase/` folder and docs onto a fresh branch.
- **User-facing status**: This branch exists but was never discussed with the user in this session. User may not be aware it is still open.

## New Handoff Template

### YYYY-MM-DD HH:MM TZ - short task name

- **Agent**: Codex / Claude / other
- **Branch or worktree**: `branch-name` or path
- **Task**: One sentence describing the goal.
- **Files touched**:
  - `path/to/file`
- **Current state**: What is done, what is partially done, and what is not started.
- **Checks run**:
  - `command` - result
- **Known issues or risks**: Anything the next agent should not rediscover.
- **Next action**: The single best next step.
- **User-facing status**: What has or has not been reported to the user.

## Completed Handoffs

Move resolved entries here only after the task is complete, merged, abandoned, or superseded.
