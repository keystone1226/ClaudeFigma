"""
Interview raw data parser.
Supports plain text, markdown, and simple structured formats.
"""
import re
import json
from pathlib import Path


def parse_interview_text(text: str) -> dict:
    """
    Parse raw interview text into structured JSON.
    Detects Q/A format, speaker labels, or plain transcript.
    """
    lines = [l.strip() for l in text.strip().splitlines() if l.strip()]

    # Try Q/A pattern: Q: ... / A: ...
    qa_pattern = re.compile(r'^(Q|A|질문|답변|interviewer|interviewee)[:\.]?\s+(.*)', re.IGNORECASE)
    # Try speaker label: "Speaker Name: ..."
    speaker_pattern = re.compile(r'^([가-힣A-Za-z\s]{1,30}):\s+(.*)')

    segments = []
    current_speaker = None
    current_lines = []

    for line in lines:
        qa_match = qa_pattern.match(line)
        speaker_match = speaker_pattern.match(line)

        if qa_match:
            if current_lines:
                segments.append({"speaker": current_speaker, "text": " ".join(current_lines)})
                current_lines = []
            role = qa_match.group(1).upper()
            if role in ("Q", "질문", "INTERVIEWER"):
                current_speaker = "interviewer"
            else:
                current_speaker = "interviewee"
            current_lines = [qa_match.group(2)]
        elif speaker_match and not line.startswith("http"):
            if current_lines:
                segments.append({"speaker": current_speaker, "text": " ".join(current_lines)})
                current_lines = []
            current_speaker = speaker_match.group(1).strip()
            current_lines = [speaker_match.group(2)]
        else:
            current_lines.append(line)

    if current_lines:
        segments.append({"speaker": current_speaker or "unknown", "text": " ".join(current_lines)})

    return {
        "raw_text": text,
        "segments": segments,
        "segment_count": len(segments),
    }


def load_interview_file(path: str) -> dict:
    """Load and parse an interview file (.txt or .md)."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {path}")
    text = p.read_text(encoding="utf-8")
    data = parse_interview_text(text)
    data["source_file"] = str(p.name)
    return data


def save_json(data: dict, output_path: str) -> None:
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved: {output_path}")
