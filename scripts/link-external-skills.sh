#!/usr/bin/env bash
# Fetch the external/ submodules (shallow) and link their SKILL.md skills into ~/.claude/skills.
# Only skills are linked; hooks, plugins and MCP servers from these repos are NOT installed.
# The first skill with a given directory name wins, so repos listed earlier take precedence.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
cd "$ROOT"
git submodule update --init --depth 1 external/ponytail external/graphify external/agent-skills \
  external/headroom external/aside-skills
# The two large repos (OmniRoute ~1.1GB, orca ~500MB) are fetched with only their skills/ folder.
for big in omniroute orca; do
  if [ ! -e "external/$big/.git" ]; then
    git submodule init "external/$big"
    url="$(git config --get "submodule.external/$big.url")"
    sha="$(git ls-tree HEAD "external/$big" | awk '{print $3}')"
    rm -rf "external/$big"
    git clone -q --depth 1 --filter=blob:none --sparse --no-checkout "$url" "external/$big"
    git -C "external/$big" sparse-checkout set skills
    git -C "external/$big" fetch -q --depth 1 origin "$sha" || true
    git -C "external/$big" checkout -q "$sha" 2>/dev/null || git -C "external/$big" checkout -q
  fi
done
mkdir -p "$DEST"
link() { # link <skill-dir> <name>
  local src="$1" name="$2"
  [ -f "$src/SKILL.md" ] || return 0
  if [ -e "$DEST/$name" ] || [ -L "$DEST/$name" ]; then return 0; fi
  ln -s "$src" "$DEST/$name" && echo "linked $name"
}
for d in external/ponytail/skills/* external/agent-skills/skills/* external/headroom/skills/* \
         external/orca/skills/* external/omniroute/skills/* external/aside-skills/*/*; do
  [ -d "$d" ] && link "$ROOT/$d" "$(basename "$d")"
done
# graphify ships its Claude skill as graphify/skill.md + skills/claude/references
G="$ROOT/external/graphify/graphify"
if [ -f "$G/skill.md" ] && [ ! -e "$DEST/graphify" ]; then
  mkdir -p "$DEST/graphify"
  ln -s "$G/skill.md" "$DEST/graphify/SKILL.md"
  ln -s "$G/skills/claude/references" "$DEST/graphify/references"
  echo "linked graphify"
fi
