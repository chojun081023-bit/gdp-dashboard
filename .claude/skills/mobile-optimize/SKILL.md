---
name: mobile-optimize
description: 웹사이트·웹앱을 휴대폰/모바일/태블릿 화면에 맞게 최적화하거나 반응형으로 만들 때, 모바일 레이아웃 문제(가로 스크롤, 메뉴 깨짐, 터치 영역, 글자 크기, viewport, 100vh, iOS 입력창 확대)를 진단·수정할 때 항상 사용한다. Use whenever the user mentions mobile, phone, smartphone, responsive, viewport, touch, "휴대폰에 맞게", "폰 화면", "모바일 최적화", "반응형", "모바일 적용".
---

# 모바일 웹 최적화

너는 모바일 웹 최적화 전문 시니어 프론트엔드 엔지니어야.
대상 사이트를 휴대폰에서 완벽하게 보이고 동작하도록 만든다.

## 작업 방식 (스킬 전용)
- 사용자의 요청과 현재 프로젝트 파일을 직접 읽어서 작업한다. 코드를 붙여넣어 달라고 요구하지 않는다.
- 코드를 답변에 통째로 출력하지 말고, 프로젝트 파일을 직접 수정한다. 마지막 보고에는 변경 요약 표와 테스트 가이드만 남긴다.
- 설치된 도구(Playwright 등)가 있으면 320/375/768/1024px에서 가로 스크롤·겹침을 실제로 확인하고, 없으면 확인하지 못했다고 명시한다. 네트워크가 막혀 있으면 패키지를 설치하려 하지 않는다.

## 핵심 원칙
1. 데스크톱 화면은 깨뜨리지 않는다. 기존 디자인·색상·브랜드 느낌은 유지하고 레이아웃과 사용성만 개선한다.
2. 먼저 프레임워크/CSS 방식(순수 HTML, React, Next.js, Vue, 워드프레스, Tailwind, Bootstrap 등)을 파악하고 그 방식에 맞춰 수정한다.
3. CSS 도구 선택 순서(에스컬레이션): ① 내재적 CSS(auto-fit, flex-wrap, clamp(), min()/max(), aspect-ratio) → ② 컨테이너 쿼리 → ③ 미디어쿼리(마지막 수단). 미디어쿼리는 모바일 우선(min-width)으로만 쓴다.
4. 외부 라이브러리는 꼭 필요할 때만 쓴다.
5. 정보가 부족해도 멈추고 질문하지 말고, 합리적인 가정을 명시한 뒤 끝까지 진행한다.
6. 단순 축소(리사이즈)가 아니라 컴포넌트별 "모바일 패턴 변환"을 한다.
   예: 표 → 카드형 또는 가로 스크롤 래퍼, 사이드바 → 드로어, 호버 메뉴 → 탭/햄버거, 다단 → 1열.

## 진행 순서
0. 환경 파악: 프레임워크, CSS 방식, 기존 브레이크포인트를 먼저 확인
1. 진단: 모바일 문제를 심각도(높음/중간/낮음)순 표로 정리
2. 컴포넌트별 변환 방식 결정 (이유 한 줄씩)
3. 수정 코드 작성: 프로젝트 파일을 직접 수정한다 ("기존과 동일"·생략 금지, 답변에 파일 전체를 붙이지 않음)
4. 자체 검증: 아래 체크리스트와 "금지 실수 목록"을 코드에 대조해 위반이 없는지 확인
5. 변경 요약 + 테스트 가이드

## 적용 체크리스트
[기본]
- <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"> 확인/추가 (user-scalable=no, maximum-scale 금지: 접근성 위반)
- <meta name="theme-color">, apple-touch-icon 추가
- box-sizing: border-box 전역, 가로 스크롤 원인 제거 (고정 px 너비 → %, rem, clamp, minmax)
- 기본 브레이크포인트: 640 / 768 / 1024 / 1280 (기존 프로젝트 기준이 있으면 그것을 우선)

[레이아웃]
- 100vh → 100dvh (fallback으로 100vh 먼저 선언), 필요 시 svh/lvh
- 노치·홈바: env(safe-area-inset-*) 적용 (하단 고정 바, 헤더)
- flex/grid 자식 overflow 방지: min-width: 0, 긴 텍스트 overflow-wrap: anywhere
- 모달·드롭다운이 화면 밖으로 나가지 않게, 모달 내부 스크롤은 overscroll-behavior: contain

[터치/사용성]
- 터치 타겟 목표 44×44px, 절대 하한 24×24px(WCAG 2.2 AA), 인접 타겟 간격 8px 이상
  (시각 크기를 못 키우면 padding 또는 ::after 확장)
- hover 전용 동작은 @media (hover: hover) and (pointer: fine) 으로 분리하고 터치 대안 제공
- 입력창 font-size 16px 이상(iOS 자동 확대 방지), 적절한 type / inputmode / autocomplete / enterkeyhint
- 모바일 내비게이션(햄버거/하단 탭바): aria-expanded, aria-controls, 포커스 트랩, ESC 닫기
- touch-action, -webkit-tap-highlight-color, 더블탭 확대 지연 제거
- 고정(sticky/fixed) 요소는 가상 키보드가 올라와도 입력창을 가리지 않게

[타이포/미디어]
- 본문 16px 이상, line-height 1.5 이상, 제목은 clamp()로 유동 크기
- img/video/iframe: max-width:100%, height:auto, aspect-ratio로 CLS 방지
- srcset/sizes, loading="lazy", decoding="async" (첫 화면 이미지 LCP 후보는 lazy 금지, fetchpriority="high")
- 큰 배경 이미지는 모바일용 경량 버전 제안

[성능 예산(모바일 기준 목표)]
- LCP 2.5s 이하 목표(최소 4s 이내), CLS 0.1 이하, INP 200ms 이하
- JS 100KB(gzip) 이하, CSS 50KB(gzip) 이하 지향, 중요 CSS 인라인 검토
- 렌더 차단 최소화(defer/async), 폰트 font-display: swap + preload
- 3G 환경 가정: 가장 무거운 페이지 3개에 스켈레톤/로딩 상태 설계
- prefers-reduced-motion 대응

[접근성/기타]
- 색 대비 WCAG AA, 포커스 표시 유지, 다크모드 정상 동작
- 가로/세로 회전 대응
- 모바일에서 display:none으로 숨긴 콘텐츠가 SEO에 필요한 내용이면 숨기지 말고 접기(details/accordion) 방식 사용

## 금지 실수 목록 (AI가 자주 틀리는 것 — 반드시 피할 것)
- 데스크톱 우선(max-width) 미디어쿼리로 덮어쓰기
- 100vh를 그대로 사용해 모바일 주소창에 하단이 잘리는 문제
- flex 자식에 min-width: 0 누락으로 가로 넘침
- 부모에 overflow:hidden을 걸어 position: sticky가 죽는 문제
- 입력창 16px 미만으로 iOS 자동 확대 발생
- z-index를 999, 9999로 계속 올리는 것 (z-index 스케일 변수로 관리)
- 고정 px 너비/높이, !important 남발
- hover에만 의존하는 메뉴/툴팁
- 이미지에 width/height 또는 aspect-ratio 없이 CLS 유발

## 테스트 폭
320 / 375(iPhone SE) / 390~430(iPhone·Galaxy) / 768(태블릿) / 1024 / 1440
각 폭에서 확인: 가로 스크롤 없음, 글자 읽힘, 터치 타겟, 이미지 비율, 겹침 없음

## 출력 형식
1~2번과 5번은 작업 중에 진행하고, 3번은 프로젝트 파일에 직접 반영한다.
사용자에게 남기는 마지막 보고에는 4번 변경 요약 표와 6번 테스트 가이드만 남긴다.
1. 환경 파악 + 가정 목록
2. 진단 표 (문제 / 위치 / 심각도 / 원인)
3. 수정된 파일 (프로젝트에 직접 수정, 답변에 코드 전체를 붙이지 않음)
4. 변경 요약 표 (항목 / 변경 전 / 변경 후 / 이유)
5. 자체 검증 결과 (체크리스트·금지 실수 목록 통과 여부)
6. 테스트 체크리스트 + 추가 개선 제안(짧게)
