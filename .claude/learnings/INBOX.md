# Learnings INBOX

Lessons gathered while working. Format: `date | situation | mistake/discovery | next time`
- Prefix 🔺 = promotion candidate (the same lesson came up 2+ times, or the user corrected it directly). Propose it to the user; do not apply it directly.
- Once promoted, move it to `PROMOTED.md` and delete it here. Contradictory or stale items: delete them, recording the reason in one line.
- Never record secrets (keys, tokens, passwords) or personal information.

| Date | Situation | Mistake/discovery | Next time |
|---|---|---|---|
| 2026-11-05 | Browser check of the Streamlit app | Waiting for the `[data-testid="stMetric"]` selector before checking succeeded. (How `networkidle` behaves with Streamlit's WebSocket is **unverified**.) | Use selector waits in browser checks |
| 2026-11-05 | Testing the whole app | `streamlit.testing.v1.AppTest.from_file()` runs the full script headlessly. The test failed as expected on a deliberately broken copy (negative check done). | Use `AppTest` instead of starting a server for logic/regression checks |
| 2026-11-05 | Bringing in external material | Part of the downloaded reference material was "All rights reserved", and this repo is public. The user then asked to remove all externally sourced material. | Do not download external material without approval; keep only self-written content |
| 2026-11-05 | Ending a turn | The Stop hook asks for files that are not yet committed to be committed and pushed. Committing before a decision is made risks irreversible exposure. | Gitignore material whose decision is pending, and leave the tree in a committable state before ending the turn |
| 2026-11-05 | Branch push from a shallow clone | With `--depth 1` the fetch refspec covers only main, so `git push -u` does not store the remote-tracking ref, and the Stop hook reported the branch as "no remote branch" | After pushing a new branch, add the refspec with `git config --add remote.origin.fetch ...`, then `git branch -u` |
| 2026-11-07 | Pushing a branch | Push was refused by the git proxy (403) because the repo was not attached to the session; `add_repo` with push access fixed it. | If a push gets a 403 from the git proxy, attach the repo with `add_repo` first |
| 2026-11-07 | Adding third-party agent tooling | OmniRoute (~1.1GB) and orca (~500MB) are too big to clone in full every session; a sparse clone of `skills/` alone took ~12s for all 7 repos. | Clone large external repos sparse, with only the folders that are needed |
| 2026-11-07 | Skill/command auto-invocation | `.claude/commands/*.md` showed up in the Skill list, so Claude could invoke them; docs say commands are merged into skills. Built-in `/compact` `/clear` are not Skill-tool invocable. | Mark user-only commands `disable-model-invocation: true`; suggest built-ins to the user instead |
| 2026-11-07 | Mobile screenshot of Streamlit | `fullPage` screenshots only the viewport because Streamlit scrolls inside `[data-testid="stMain"]`; `st.columns` stacks one per line under ~640px. | Resize the viewport to `stMain.scrollHeight` before shooting; use `st.container(horizontal=True)` for cards that should stay side by side |
