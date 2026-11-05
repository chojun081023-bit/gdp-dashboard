#!/usr/bin/env bash
# SessionStart: show the latest lessons and promotion-candidate count to Claude. Read-only.
I="$CLAUDE_PROJECT_DIR/.claude/learnings/INBOX.md"
[ -f "$I" ] || exit 0
echo "Recent lessons (.claude/learnings/INBOX.md):"
grep -E '^\| (🔺 )?20[0-9]{2}-' "$I" | tail -n 5 | cut -c1-220
echo "Promotion candidates (🔺): $(grep -c '^| 🔺' "$I")"
