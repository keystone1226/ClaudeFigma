#!/usr/bin/env python3
"""
Interview Raw Data → JSON → FigJam 다이어그램 변환 CLI

사용법:
    python main.py <interview_file> [--output-dir OUTPUT_DIR]

예시:
    python main.py examples/sample_interview.txt
    python main.py examples/sample_interview.txt --output-dir ./output
"""
import argparse
import sys
from pathlib import Path

from src.parser import load_interview_file, save_json
from src.analyzer import analyze_interview
from src.figjam_exporter import export_figjam_json


def main():
    parser = argparse.ArgumentParser(
        description="인터뷰 raw data를 JSON + FigJam 다이어그램으로 변환합니다."
    )
    parser.add_argument("interview_file", help="인터뷰 파일 경로 (.txt 또는 .md)")
    parser.add_argument(
        "--output-dir", default="output",
        help="결과 파일 저장 디렉토리 (기본값: ./output)"
    )
    args = parser.parse_args()

    source_path = Path(args.interview_file)
    output_dir = Path(args.output_dir)
    stem = source_path.stem

    # 1. Parse raw interview text → JSON
    print(f"\n[1/3] 인터뷰 파일 파싱 중: {source_path}")
    parsed = load_interview_file(str(source_path))
    parsed_json_path = output_dir / f"{stem}_parsed.json"
    save_json(parsed, str(parsed_json_path))
    print(f"      세그먼트 수: {parsed['segment_count']}")

    # 2. Analyze with Claude API → pain points + key findings
    print("\n[2/3] Claude API로 분석 중 (pain points, 주요 발견점)...")
    try:
        analysis = analyze_interview(parsed)
    except ValueError as e:
        print(f"\n오류: {e}", file=sys.stderr)
        print("ANTHROPIC_API_KEY 환경변수를 설정해 주세요.", file=sys.stderr)
        sys.exit(1)

    analysis_json_path = output_dir / f"{stem}_analysis.json"
    save_json(analysis, str(analysis_json_path))
    print(f"      Pain points: {len(analysis.get('pain_points', []))}")
    print(f"      Key findings: {len(analysis.get('key_findings', []))}")

    # 3. Export FigJam JSON
    print("\n[3/3] FigJam JSON 생성 중...")
    figjam_json_path = output_dir / f"{stem}_figjam.json"
    export_figjam_json(analysis, str(figjam_json_path), source_name=stem)

    print(f"\n완료! 결과 파일:")
    print(f"  - 파싱 결과:    {parsed_json_path}")
    print(f"  - 분석 결과:    {analysis_json_path}")
    print(f"  - FigJam JSON: {figjam_json_path}")
    print("\nFigJam 사용법: FigJam 파일 열기 → Plugins → Widget으로 JSON 불러오기")


if __name__ == "__main__":
    main()
