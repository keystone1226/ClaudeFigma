"""
분석 결과를 FigJam 호환 JSON 형식으로 변환합니다.

FigJam REST API의 /v1/files/:file_key/nodes 엔드포인트에서 사용 가능한
sticky note + connector 구조로 출력합니다.
참고: https://www.figma.com/developers/api#files
"""

import json
from typing import Any


# Color palette for severity / category
COLORS = {
    # Pain point severity
    "high":    {"r": 1.0,  "g": 0.31, "b": 0.31, "a": 1},  # red
    "medium":  {"r": 1.0,  "g": 0.76, "b": 0.24, "a": 1},  # orange
    "low":     {"r": 0.55, "g": 0.83, "b": 0.55, "a": 1},  # green
    # Key finding categories
    "behavior": {"r": 0.53, "g": 0.74, "b": 0.97, "a": 1},  # blue
    "attitude": {"r": 0.85, "g": 0.65, "b": 0.97, "a": 1},  # purple
    "need":     {"r": 0.97, "g": 0.91, "b": 0.53, "a": 1},  # yellow
    "context":  {"r": 0.72, "g": 0.97, "b": 0.87, "a": 1},  # teal
    # Default
    "default":  {"r": 0.95, "g": 0.95, "b": 0.95, "a": 1},
}

# Layout constants (pixels)
STICKY_W = 300
STICKY_H = 160
GAP_X = 40
GAP_Y = 60
START_X = 100
START_Y = 100
SECTION_GAP_Y = 120


def _sticky(node_id: str, x: float, y: float, label: str, body: str, color: dict) -> dict:
    """Create a FigJam sticky note node dict."""
    return {
        "id": node_id,
        "type": "STICKY",
        "name": label,
        "absoluteBoundingBox": {"x": x, "y": y, "width": STICKY_W, "height": STICKY_H},
        "fills": [{"type": "SOLID", "color": color}],
        "characters": f"**{label}**\n{body}",
    }


def _section_header(node_id: str, x: float, y: float, title: str) -> dict:
    """Create a text label for a section."""
    return {
        "id": node_id,
        "type": "TEXT",
        "name": title,
        "absoluteBoundingBox": {"x": x, "y": y, "width": 600, "height": 40},
        "characters": title,
        "style": {"fontFamily": "Inter", "fontSize": 24, "fontWeight": "Bold"},
        "fills": [{"type": "SOLID", "color": {"r": 0.1, "g": 0.1, "b": 0.1, "a": 1}}],
    }


def build_figjam_document(analysis: dict, source_name: str = "interview") -> dict:
    """
    analysis dict (from analyzer.py) → FigJam-compatible node list.

    Returns a dict with:
      - document_name
      - nodes: list of FigJam node dicts
    """
    nodes: list[dict[str, Any]] = []
    node_counter = 1

    def nid() -> str:
        nonlocal node_counter
        _id = f"node-{node_counter:04d}"
        node_counter += 1
        return _id

    current_y = START_Y

    # ── Summary banner ──────────────────────────────────────────────────
    summary = analysis.get("summary", "")
    if summary:
        nodes.append(_section_header(nid(), START_X, current_y, "📋 인터뷰 요약"))
        current_y += 50
        nodes.append(_sticky(
            nid(), START_X, current_y, source_name, summary,
            COLORS["default"]
        ))
        current_y += STICKY_H + SECTION_GAP_Y

    # ── Pain Points ──────────────────────────────────────────────────────
    pain_points = analysis.get("pain_points", [])
    if pain_points:
        nodes.append(_section_header(nid(), START_X, current_y, "🔴 사용자 Pain Points"))
        current_y += 50
        col = 0
        row_start_y = current_y
        for pp in pain_points:
            x = START_X + col * (STICKY_W + GAP_X)
            y = row_start_y
            color = COLORS.get(pp.get("severity", ""), COLORS["default"])
            body = pp.get("description", "")
            quotes = pp.get("quotes", [])
            if quotes:
                body += f"\n\n💬 \"{quotes[0]}\""
            severity_label = pp.get("severity", "").upper()
            nodes.append(_sticky(
                nid(), x, y,
                f"[{severity_label}] {pp.get('title', '')}",
                body, color
            ))
            col += 1
            if col >= 4:
                col = 0
                row_start_y += STICKY_H + GAP_Y
        current_y = row_start_y + STICKY_H + SECTION_GAP_Y

    # ── Key Findings ─────────────────────────────────────────────────────
    key_findings = analysis.get("key_findings", [])
    if key_findings:
        nodes.append(_section_header(nid(), START_X, current_y, "💡 주요 발견점"))
        current_y += 50
        col = 0
        row_start_y = current_y
        for kf in key_findings:
            x = START_X + col * (STICKY_W + GAP_X)
            y = row_start_y
            category = kf.get("category", "")
            color = COLORS.get(category, COLORS["default"])
            body = kf.get("description", "")
            evidence = kf.get("evidence", [])
            if evidence:
                body += f"\n\n📌 \"{evidence[0]}\""
            cat_label = category.upper() if category else "FINDING"
            nodes.append(_sticky(
                nid(), x, y,
                f"[{cat_label}] {kf.get('title', '')}",
                body, color
            ))
            col += 1
            if col >= 4:
                col = 0
                row_start_y += STICKY_H + GAP_Y
        current_y = row_start_y + STICKY_H + SECTION_GAP_Y

    # ── User Goals ───────────────────────────────────────────────────────
    user_goals = analysis.get("user_goals", [])
    if user_goals:
        nodes.append(_section_header(nid(), START_X, current_y, "🎯 사용자 목표 / 니즈"))
        current_y += 50
        goals_text = "\n".join(f"• {g}" for g in user_goals)
        nodes.append(_sticky(
            nid(), START_X, current_y, "User Goals", goals_text,
            COLORS["need"]
        ))

    return {
        "document_name": f"Interview Analysis — {source_name}",
        "nodes": nodes,
        "node_count": len(nodes),
    }


def export_figjam_json(analysis: dict, output_path: str, source_name: str = "interview") -> None:
    """Save FigJam-compatible JSON to file."""
    from pathlib import Path
    doc = build_figjam_document(analysis, source_name)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    print(f"FigJam JSON saved: {output_path}  ({doc['node_count']} nodes)")
