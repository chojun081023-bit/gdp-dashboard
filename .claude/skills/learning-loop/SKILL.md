---
name: learning-loop
description: Run this every time you finish a task in this repository (a feature addition, bug fix, test, or review) — before the final report. Also use it right away when the user corrects you (e.g. "아니", "그게 아니라", "틀렸어", "다시 해", "더 짧게"), when you hit a blocker and change approach, or when you find a new project rule. Records lessons in .claude/learnings/INBOX.md and proposes promotion candidates to the user.
---

# Learning loop

## Before finishing a task

1. **Record**: if any of the following happened, add one row to `.claude/learnings/INBOX.md` as `date | situation | mistake/discovery | next time`.
   - A blocker, a mistake you then fixed, a newly found project rule, a correction from the user, a skill or description that misfired
   - Put unverified facts in the row with "(미검증)" (unverified) appended. No secrets or personal information.
2. **Mark candidates**: prefix 🔺 when the same lesson exists at least twice, or when the user corrected you directly.
3. **Propose**: if there are 🔺 rows, propose them in one line at the end of the report. Include the exact change (CLAUDE.md diff, a new skill draft, or a profile.md edit). **Do not apply directly.**
4. **Apply after approval**: once approved, apply the change, move the row to `PROMOTED.md`, and delete it from INBOX.

## Capability growth signals (propose only)

- Same procedure performed 3+ times → propose a skill or slash command
- A separable role (review, tests, docs) → propose a subagent
- New dependency, MCP server, or hook → explain why and the risks, then get approval. For hooks, show the JSON diff first.

## Cleanup

- If CLAUDE.md goes over 150 lines, or a section grows past 20 lines, propose moving it into a skill.
- When the user asks, or about once a month: propose a cleanup of unused skills, conflicting rules, and stale lessons (more than 60 days old and never repeated).
- Do not download external material (repositories, prompts, skills) without the user's approval.

## Writing a new skill, command, or agent

- The `description` is the trigger: write concrete situations ("Use when ..."), put every "when to use" condition there, not in the body.
- Keep the body short; no network calls, `shell=True`, or file deletion in bundled scripts.
- Subagents: state the invocation condition in the description and grant only the tools the role needs.
- After writing, simulate 2–3 representative requests; if it would not trigger, revise the description and record it in INBOX.
