# Learnings INBOX

Lessons gathered while working. Format: `date | situation | mistake/discovery | next time`
- Prefix 🔺 = promotion candidate (the same lesson came up 2+ times, or the user corrected it directly). Propose it to the user; do not apply it directly.
- Once promoted, move it to `PROMOTED.md` and delete it here. Contradictory or stale items: delete them, recording the reason in one line.
- Never record secrets (keys, tokens, passwords) or personal information.

| Date | Situation | Mistake/discovery | Next time |
|---|---|---|---|
| 2026-11-05 | Browser check of the Streamlit app | Waiting for the `[data-testid="stMetric"]` selector before checking succeeded. (How `networkidle` behaves with Streamlit's WebSocket is **unverified**.) | Use selector waits in browser checks |
| 2026-11-05 | Testing the whole app | `streamlit.testing.v1.AppTest.from_file()` runs the full script headlessly. The test failed as expected on a deliberately broken copy (negative check done). | Use `AppTest` instead of starting a server for logic/regression checks |
| 2026-11-05 | Bringing in external material | `anthropics/claude-code` and the `docx/pdf/pptx/xlsx` skills are "All rights reserved", and this repo is public | Check the license before vendoring; commit only `SOURCES.md` |
| 2026-11-05 | Ending a turn | The Stop hook asks for files that are not yet committed to be committed and pushed. Committing before a decision is made risks irreversible exposure. | Gitignore material whose decision is pending, and leave the tree in a committable state before ending the turn |
