---
name: test-observer
description: Use whenever you run this repo's tests, or the user asks whether tests pass, why a test failed, or to "watch"/"observe" the test run. Runs pytest and returns a short report (counts, failing test names) with long failure output compressed by headroom so error lines stay and noise goes, instead of reading raw pytest output.
---

# Test observer

```bash
. .venv/bin/activate          # needs requirements-dev.txt (pytest, headroom-ai)
python .claude/skills/test-observer/scripts/observe_tests.py          # whole suite
python .claude/skills/test-observer/scripts/observe_tests.py tests/test_app_smoke.py -k metric
```

- Extra arguments go straight to pytest. The exit code is pytest's.
- Output: `pytest exit N: X passed · Y failed`, one `FAIL <nodeid>` line per failure, then the failure
  output. Output over 4000 chars is compressed with headroom (`HEADROOM_OFFLINE=1`, no network);
  without headroom only the tail is shown.
- Read the report, not the raw run. If the compressed output hides what you need, rerun that one test
  with `python -m pytest <nodeid> -x`.

## Report

One line: `pytest N passed / M failed` plus the failing test names, if any.
