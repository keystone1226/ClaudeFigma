"""
Claude API를 사용해 인터뷰 데이터에서 pain points와 주요 발견점을 추출합니다.
"""
import json
import os
import anthropic


ANALYSIS_PROMPT = """\
다음은 사용자 인터뷰 내용입니다. 아래 항목들을 추출하여 JSON으로 반환해 주세요.

인터뷰 내용:
{interview_text}

다음 JSON 형식으로만 응답하세요 (설명 없이):
{{
  "pain_points": [
    {{
      "id": "pp1",
      "title": "pain point 제목 (간결하게)",
      "description": "구체적인 설명",
      "severity": "high | medium | low",
      "quotes": ["관련 인터뷰 인용문"]
    }}
  ],
  "key_findings": [
    {{
      "id": "kf1",
      "title": "발견점 제목",
      "description": "상세 설명",
      "category": "behavior | attitude | need | context",
      "evidence": ["근거 인용문"]
    }}
  ],
  "user_goals": ["사용자의 주요 목표/니즈"],
  "summary": "인터뷰 전체 요약 (2-3문장)"
}}"""


def analyze_interview(parsed_data: dict, api_key: str | None = None) -> dict:
    """
    Claude API로 인터뷰 데이터를 분석해 pain points와 주요 발견점을 반환합니다.
    """
    key = api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise ValueError("ANTHROPIC_API_KEY 환경변수가 필요합니다.")

    # Build interview text from segments
    segments = parsed_data.get("segments", [])
    if segments:
        interview_text = "\n".join(
            f"[{s['speaker']}] {s['text']}" for s in segments
        )
    else:
        interview_text = parsed_data.get("raw_text", "")

    client = anthropic.Anthropic(api_key=key)
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": ANALYSIS_PROMPT.format(interview_text=interview_text),
            }
        ],
    )

    response_text = message.content[0].text.strip()

    # Extract JSON from response (in case there's extra text)
    json_start = response_text.find("{")
    json_end = response_text.rfind("}") + 1
    analysis = json.loads(response_text[json_start:json_end])

    return analysis
