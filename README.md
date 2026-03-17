# ClaudeFigma

인터뷰 raw data를 JSON으로 변환하고, Claude AI로 분석해 **FigJam 다이어그램**, **사용자 Pain Points**, **주요 발견점**으로 정리합니다.

## 흐름

```
인터뷰 .txt/.md
      │
      ▼
[1] parser.py       → {stem}_parsed.json    (세그먼트 구조화)
      │
      ▼
[2] analyzer.py     → {stem}_analysis.json  (Claude API 분석)
   ┌──────────────────────────────────────┐
   │  pain_points  (severity: high/medium/low)  │
   │  key_findings (category: behavior/attitude/need/context) │
   │  user_goals                           │
   │  summary                              │
   └──────────────────────────────────────┘
      │
      ▼
[3] figjam_exporter.py → {stem}_figjam.json (FigJam sticky note 레이아웃)
```

## 설치

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-api-key"
```

## 사용법

```bash
python main.py examples/sample_interview.txt
python main.py my_interview.md --output-dir ./results
```

## 출력 파일

| 파일 | 내용 |
|------|------|
| `{stem}_parsed.json` | 인터뷰 세그먼트 (speaker + text) |
| `{stem}_analysis.json` | Pain points, 주요 발견점, 사용자 목표, 요약 |
| `{stem}_figjam.json` | FigJam sticky note 노드 레이아웃 |

## FigJam에 적용하기

1. FigJam 파일 열기
2. **Plugins** → **JSON to FigJam** (또는 커스텀 Widget 사용)
3. `{stem}_figjam.json` 파일 불러오기

또는 [Figma REST API](https://www.figma.com/developers/api)를 통해 자동으로 노드를 생성할 수 있습니다.

## 인터뷰 파일 형식

**Q/A 형식 (권장)**
```
Q: 질문 내용
A: 답변 내용
```

**화자 레이블 형식**
```
인터뷰어: 질문 내용
참여자: 답변 내용
```

**자유 텍스트**
형식이 없어도 그대로 분석됩니다.

## 분석 결과 구조

```json
{
  "pain_points": [
    {
      "id": "pp1",
      "title": "pain point 제목",
      "description": "상세 설명",
      "severity": "high | medium | low",
      "quotes": ["관련 인용문"]
    }
  ],
  "key_findings": [
    {
      "id": "kf1",
      "title": "발견점 제목",
      "description": "상세 설명",
      "category": "behavior | attitude | need | context",
      "evidence": ["근거 인용문"]
    }
  ],
  "user_goals": ["사용자 목표"],
  "summary": "전체 요약"
}
```
