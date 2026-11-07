# external/ — third-party agent tooling (git submodules)

These are **references to upstream repositories**, not copies. Each folder is a shallow git
submodule pinned to a commit; the code stays under its own license in its own repo.

| Folder | Upstream | What it is | License |
|---|---|---|---|
| `ponytail` | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | "Laziest senior dev" skills: YAGNI-first code, `/ponytail-review`, `/ponytail-audit` | MIT |
| `omniroute` | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | Multi-provider AI gateway (routing, fallback, compression) + `omni-*`/`cli-*` skills | MIT |
| `graphify` | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Codebase → queryable knowledge graph, `/graphify` skill | see repo LICENSE |
| `agent-skills` | [anthropics/skills](https://github.com/anthropics/skills) | Anthropic's public Agent Skills (docx, pdf, pptx, xlsx, skill-creator, mcp-builder …) | per-skill |
| `orca` | [stablyai/orca](https://github.com/stablyai/orca) | Run a fleet of coding agents; `orca-*` skills | MIT |
| `headroom` | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Compress tool outputs/logs/RAG chunks before they reach the LLM | Apache-2.0 |
| `aside-skills` | [anthonycho-ux/aside-skills](https://github.com/anthonycho-ux/aside-skills) | Community skills for the Aside agent browser (Aside itself is not open source). Currently one skill: `canadian-corporate-tax` | none stated |

## Use

```bash
scripts/link-external-skills.sh   # fetch submodules + symlink skills into ~/.claude/skills
```

- OmniRoute (~1.1 GB) and orca (~500 MB) are fetched sparse: only their `skills/` folder.
  For the full app: `git submodule update --init external/omniroute`.
- Only `SKILL.md` skills are linked. Hooks, plugins, status bands and MCP servers from these repos
  are **not** installed. If two repos ship a skill with the same folder name, the first one wins
  (order: ponytail, anthropics, headroom, orca, omniroute, aside, graphify).
- CLIs (optional, not installed by the script): `uv tool install graphifyy && graphify install`,
  `pip install headroom-ai`.

## Update to upstream latest

```bash
git submodule update --remote --depth 1 external/<name> && git add external/<name>
```
