---
name: verify-app
description: Use after any change to streamlit_app.py, data/, or requirements*.txt, and before reporting a feature addition or bug fix as done — runs tests, lint, and a headless run of the actual app, then checks the rendered page for exceptions. Also use when the user asks to run, check, screenshot, or "see if the dashboard works".
---

# Verify the app

Source: the "inspect first, then act" pattern from `anthropics/skills` → `skills/webapp-testing/SKILL.md` (Apache-2.0, commit `ca45fc4`), rewritten.
Not adopted: the original's `with_server.py` (it runs arbitrary commands with `shell=True`) and its "run without reading the source" guidance.

## Steps (stop at the first failure and report it)

```bash
. .venv/bin/activate                  # if missing: python3 -m venv .venv && pip install -r requirements-dev.txt
ruff check . && ruff format --check .
python -m pytest -q
```

For UI changes, also check the rendered output:

```bash
streamlit run streamlit_app.py --server.headless true --server.port 8501 &
curl -s http://localhost:8501/_stcore/health     # expect "ok"
node .claude/skills/verify-app/scripts/check_render.js http://localhost:8501
```

- `check_render.js` waits for the `[data-testid="stMetric"]` selector, then prints the counts of metric cards and exceptions (`stException`). It exits with status 1 if there is even one exception.
- Requires Node with `playwright` available. If it is not, skip this step and say "렌더 확인 생략(Playwright 없음)" (render check skipped, Playwright unavailable).
- Stop the server when you are done (only the process you started).

## Report

One line: `ruff OK · pytest N passed · render: metrics M, exceptions 0`
