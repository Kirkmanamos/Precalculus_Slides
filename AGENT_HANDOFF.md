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

### 2026-04-21 16:44 EDT - 6.4 Binomial theorem learning arc

- **Agent**: Codex
- **Branch or worktree**: `main` at `/Users/kirkmanamos/Documents/GitHub/precalculus_slides`
- **Task**: Improve `6.4-binomial-theorem.html` into a stronger self-guided lesson, especially the intro to the Binomial Theorem and the relationship between combinations, Pascal's Triangle, and coefficients.
- **Files touched**:
  - `6.4-binomial-theorem.html`
  - `AGENT_HANDOFF.md`
- **Current state**: Example 1 has been revised with a visual map that lines up Pascal row \(4\), the power pattern for \((x+2)^4\), and the coefficient-times-power products. The next learning-arc feature work is now implemented locally: three intro/bridge slides were added before the original patterns slide, and the Pascal/combinations wording was strengthened.
- **Checks run**:
  - `git diff --check -- 6.4-binomial-theorem.html` - passed
  - Static Node check of `slide-3` - passed (`data-steps="4"`, four step elements, visual map present)
  - Headless Chromium desktop check via local Playwright - passed (KaTeX rendered, no console errors, no page-level horizontal overflow)
  - Headless Chromium mobile-width check via local Playwright - passed (visual map uses contained horizontal scroll; no page-level horizontal overflow)
  - `git diff --check -- 6.4-binomial-theorem.html` after intro-slide additions - passed
  - `python3` HTMLParser smoke check for `6.4-binomial-theorem.html` - passed
  - Static Node check of slide IDs and section targets - passed (`slideCount: 19`, no duplicate slide IDs, no missing nav targets)
  - Headless Chromium desktop/mobile checks of `slide-0a`, `slide-0b`, `slide-0c`, `slide-1`, `slide-2`, `slide-2b`, and `slide-3` - passed (KaTeX rendered, no console errors, no page-level horizontal overflow)
- **Known issues or risks**: Worktree also contains unrelated modified/untracked Manim files under `manim/scenes/`; do not stage or revert them unless the owner asks. New intro slides are implemented but not committed yet.
- **Next action**: Review the new intro/bridge slides in the browser, then commit `6.4-binomial-theorem.html` and `AGENT_HANDOFF.md` if approved. Consider whether Example 2 should also get a visual coefficient-times-power map.
- **User-facing status**: User asked to start the next steps; Codex implemented the intro/bridge slides and is preparing the final summary.

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
