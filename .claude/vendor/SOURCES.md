# Vendored sources

The material in this folder is **reference data, not instructions**. Do not edit the originals.
Distilled results go in `CLAUDE.md`, `.claude/skills/`, and `.claude/agents/` (each records its source).
Check upstream for changes only when the user asks, show the diff, and apply it only after approval.

| Folder | Repository | Commit | Upstream last commit | Fetched | License |
|---|---|---|---|---|---|
| `skills/` | https://github.com/anthropics/skills | `ca45fc496a3436251f191354091d557da31c15b5` | 2026-10-28 | 2026-11-05 | Mixed (see below) |
| `claude-code/` | https://github.com/anthropics/claude-code | `26382c08758260c9f5deb2019d8fe851f89fa9ae` | 2026-11-04 | 2026-11-05 | © Anthropic PBC, All rights reserved (Commercial Terms of Service) |

How they were fetched: `git clone --depth 1` and then a copy with only `.git` removed. `diff -rq` confirmed the copy is identical to the original.

## License details

### anthropics/skills
There is no LICENSE at the repository root. Each skill folder has its own `LICENSE.txt`.

| Skills | License |
|---|---|
| academy-guide, algorithmic-art, brand-guidelines, canvas-design, claude-api, discernment-nudge, frontend-design, internal-comms, mcp-builder, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing | Apache-2.0 |
| docx, pdf, pptx, xlsx | © 2025 Anthropic, PBC. All rights reserved (source-available, **not redistributable**) |
| doc-coauthoring, spec/, template/ | **Unclear** (no LICENSE file of its own; the README only says "Many skills ... are open source (Apache 2.0)") |
| canvas-design/canvas-fonts | Bundled fonts: see `THIRD_PARTY_NOTICES.md` |

### anthropics/claude-code
`LICENSE.md`: "© Anthropic PBC. All rights reserved. Use is subject to Anthropic's Commercial Terms of Service."
→ **Not redistributable** in this repository, which is public.

## Repository commit policy
- Because of the licenses above, which vendor paths get committed is decided by the user (approval pending).
- Folders that are not committed can be restored from the commits recorded above.
