#!/usr/bin/env bash
# UserPromptSubmit: if the prompt is about mobile/responsive work, remind Claude to call the mobile-optimize skill.
# Prints one line (added to Claude's context) on a match, nothing otherwise. Never blocks: always exit 0.
input=$(cat)
prompt=$(printf '%s' "$input" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("prompt", ""))' 2>/dev/null) \
  || prompt=$input  # no python3 or bad JSON: match against the raw payload
if printf '%s' "$prompt" | grep -qiE '모바일|휴대폰|스마트폰|폰 화면|폰에|태블릿|반응형|가로 스크롤|터치|mobile|phone|responsive|viewport'; then
  echo '모바일/반응형 요청입니다: 코드를 수정하기 전에 mobile-optimize 스킬을 먼저 호출하고 그 절차를 따르세요.'
fi
exit 0
