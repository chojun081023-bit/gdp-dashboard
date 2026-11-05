#!/usr/bin/env bash
# PostToolUse(Edit|Write): format the edited .py file and sort its imports with ruff.
# Never deletes code (unused imports are left alone), never blocks, no network.
# Full lint runs in the verify-app skill.
f=$(python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input", {}).get("file_path", ""))' 2>/dev/null)
case "$f" in *.py) ;; *) exit 0 ;; esac
ruff="$CLAUDE_PROJECT_DIR/.venv/bin/ruff"
[ -x "$ruff" ] || exit 0
cd "$CLAUDE_PROJECT_DIR" || exit 0
"$ruff" check --force-exclude --select I --fix -q "$f" >/dev/null 2>&1
"$ruff" format --force-exclude -q "$f" >/dev/null 2>&1
exit 0
