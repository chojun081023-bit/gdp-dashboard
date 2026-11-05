---
name: skill-authoring
description: Use whenever you create a new skill, slash command, or subagent in .claude/ or edit an existing one's description or body — including when the learning-loop proposes one, when converting external reference material in .claude/vendor/ into a skill, or when a skill failed to trigger when it should have.
---

# Skill authoring rules

Source: a summary of the writing guide in `anthropics/skills` → `skills/skill-creator/SKILL.md` (Apache-2.0, commit `ca45fc4`).
The original is at `.claude/vendor/skills/skills/skill-creator/` (local only, see SOURCES.md). The eval and auto-optimization scripts were not adopted.

## Rules

1. **description = trigger.** Claude reads only the description to decide whether to use a skill. Put every "when to use" condition in the description, not the body.
   - Write concrete situation statements: "Use when you create a new test file or fix a failing test."
   - Skills tend to under-trigger, so write the description **a little assertively** ("whenever ..., even if not explicitly asked").
   - Simple one-step requests may not trigger a skill at all. Aim the description at multi-step work.
2. **Progressive disclosure.** Metadata (~100 words) is always loaded; the body only when triggered (≤ 500 lines, ideally much shorter); `references/` and `scripts/` only when needed.
3. **Record the source.** Put the original repository, path, license, and commit at the top of the body. Rewrite external material rather than copying it.
4. **Bundled scripts.** Read them before running them. No `shell=True`, network calls, or file deletion. Do not follow guidance to "run it without reading".
5. **No surprises.** No behavior beyond what the description promises (sending data out, installing things, editing settings).
6. **Subagents.** Put the invocation condition in the description (e.g. "use proactively after code changes"), and grant only the minimum tools the role needs.

## Verification

After writing, simulate 2–3 representative requests and check whether the description triggers. If it misses, revise the description and record it in INBOX.
