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

No active handoffs.

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
