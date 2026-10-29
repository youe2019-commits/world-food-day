# 한입의 세계 · 세계 음식의 날

중학교 1학년 사회 45분 수업을 위한 교사용 웹 화면과 종이 학습지입니다.

## 사용

- 웹: https://youe2019-commits.github.io/world-food-day/
- `downloads/student-set.pdf`: 읽기 자료 1쪽 + 활동지 2쪽
- `downloads/worksheet.pdf`: 활동지만 2쪽
- `downloads/teacher-guide.pdf`: 수업 운영 가이드 2쪽
- 단계별 이동, 집중 모드, 발언 타이머(1·2·3분), PDF 다운로드 제공
- 서버·로그인·외부 라이브러리 없이 실행됩니다. 학생 답안을 수집하지 않습니다.

## 교육과정

[9사(일사)02-03] 여러 집단에서 나타나는 다양한 문화 사례들을 조사하고, 문화를 이해하는 바람직한 태도에 대하여 토의한다.

교육과정 MCP `get_standard`에서 원문 확인(2026-10-28). 국가교육위원회 고시 제2024-3호 별책 7 사회과 교육과정, PDF 62쪽.

## 자료 출처

- UNESCO [김장](https://ich.unesco.org/en/RL/kimjang-making-and-sharing-kimchi-in-the-republic-of-korea-00881)
- UNESCO [멕시코 전통 음식](https://ich.unesco.org/en/RL/traditional-mexican-cuisine-ancestral-ongoing-community-culture-the-michoacan-paradigm-00400)

소개 글은 중1 수준에 맞춰 재구성했습니다. 상황과 학생 대사는 수업용 가상 내용입니다. 문화 존중과 음식 섭취 강요를 구분하며, 개인의 식생활·건강·가정 배경 공개를 요구하지 않습니다.

## 그림

`assets/cafeteria.webp`는 내장 ImageGen으로 생성했습니다. 원본 PNG는 로컬 프로젝트에 보관합니다.

생성 프롬프트:

> Use case: illustration-story. Asset: wide classroom discussion illustration for Korean middle school grade 1 social studies website and printed worksheet. Scene: modern Korean school cafeteria, four young teenage students in everyday school uniforms around one lunch table with trays containing different international foods. Two students look excited and curious, one hesitates thoughtfully about unfamiliar food, one mediates with open hands. Make disagreement visible through facial expression, no hostility, no ridicule. Warm stylish editorial webtoon illustration with thick clean dark outlines, cream background, violet and orange accents, sophisticated playful school magazine style. Landscape 3:2. No text, no lettering, no speech bubbles, no flags, no stereotypes, no watermark.

## 수정 및 배포

정적 파일을 `main` 브랜치 루트에 배치하고 GitHub Pages의 `Deploy from a branch / main / root`를 사용합니다. PDF 생성 원본 `build_pdf.py`는 Windows 맑은 고딕 글꼴과 reportlab, pymupdf, pillow를 사용합니다. 다른 운영체제에서는 글꼴 경로를 변경해야 합니다.

수업 흐름: 상황 5분 → 문화 자료 조사 10분 → 근거 토론 12분 → 공동 제안 13분 → 성찰 5분.
