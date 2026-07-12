#!/usr/bin/env python3
"""Generate the awesome-list README from data/papers.json."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPERS_PATH = ROOT / "data" / "papers.json"
README_PATH = ROOT / "README.md"

CATEGORY_ORDER = [
    ("motion-retargeting-and-tracking", "Motion Retargeting and Tracking"),
    ("skill-acquisition", "Skill Acquisition"),
    ("interaction-learning", "Interaction Learning"),
    ("generalist-humanoid-policies", "Generalist Humanoid Policies"),
]

CATEGORY_SCOPE = {
    "motion-retargeting-and-tracking": (
        "Human-to-Humanoid motion retargeting, and physics-based reference tracking."
    ),
    "skill-acquisition": (
        "humanoid skills such as sports, acrobatics, and long-horizon behavior."
    ),
    "interaction-learning": "Object, scene, and human interaction behaviors.",
    "generalist-humanoid-policies": (
        "General strategies encompassing versatile skill mastery, multi-task adaptability, and situational flexibility."
    ),
}

SUBCATEGORY_ORDER = {
    "motion-retargeting-and-tracking": [
        ("motion-retargeting", "Motion Retargeting"),
        ("physics-based-motion-tracking", "Physics-based Motion Tracking"),
    ],
    "skill-acquisition": [
        ("sports-skills", "Sports Skills"),
        ("acrobatic-skills", "Acrobatic Skills"),
        ("long-horizon-skills", "Long-Horizon Skills"),
    ],
    "interaction-learning": [
        ("humanoid-object-interaction", "Humanoid-Object Interaction"),
        ("humanoid-scene-interaction", "Humanoid-Scene Interaction"),
        ("humanoid-human-interaction", "Humanoid-Human Interaction"),
    ],
    "generalist-humanoid-policies": [
        ("skill-guided-policies", "Skill-Guided Policies"),
        ("task-guided-policies", "Task-Guided Policies"),
        ("vision-language-guided-policies", "Vision-Language-Guided Policies"),
    ],
}


def paper_line(paper: dict) -> str:
    venue = f"{paper['venue']} {paper['year']}"
    paper_url = paper.get("links", {}).get("paper", "")
    venue_part = f"[{venue}]({paper_url})" if paper_url else venue

    method = paper.get("method_name", paper["title"])
    title = paper["title"]
    extras = []

    project = paper.get("links", {}).get("project", "")
    code = paper.get("links", {}).get("code", "")
    if project:
        extras.append(f"[website]({project})")
    if code:
        extras.append(f"[code]({code})")

    suffix = f", {' / '.join(extras)}" if extras else ""
    return f"- {venue_part}, **{method}**: {title}{suffix}"


def main() -> int:
    data = json.loads(PAPERS_PATH.read_text(encoding="utf-8"))

    lines = [
        "# Awesome Humanoid Imitation Learning Survey",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) "
        "[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]"
        "(http://makeapullrequest.com)",
        "",
        "![Method Taxonomy](assets/years.png)",
        "",
        "This repository collects papers from **A Survey of Humanoid Imitation Learning** "
        "and organizes them according to the survey's **Methods of Humanoid Imitation Learning** "
        "taxonomy.",
        "",
        "Supporting metadata is kept in `data/papers.json`, but the README classification "
        "follows only the method categories and subcategories used in the paper.",
        "",
        "## Contents",
        "",
    ]

    lines.append("- [Awesome Humanoid Imitation Learning](#awesome-humanoid-imitation-learning)")
    for _, name in CATEGORY_ORDER:
        anchor = name.lower().replace(" ", "-")
        lines.append(f"  - [{name}](#{anchor})")
    lines.extend(["- [Data Format](#data-format)", "", "---", ""])
    lines.extend(["## Awesome Humanoid Imitation Learning", ""])

    for category_id, category_name in CATEGORY_ORDER:
        category_papers = [p for p in data["papers"] if p["primary_category"] == category_id]
        lines.extend([f"### {category_name}", "", CATEGORY_SCOPE[category_id], ""])

        for subcategory_id, subcategory_name in SUBCATEGORY_ORDER[category_id]:
            papers = [p for p in category_papers if p.get("subcategory") == subcategory_id]
            if not papers:
                continue
            lines.extend([f"#### {subcategory_name}", ""])
            for paper in sorted(
                papers, key=lambda p: (p["year"], p["venue"], p.get("method_name", p["title"]).lower())
            ):
                lines.append(paper_line(paper))
            lines.append("")

    lines.extend(
        [
            "## Data Format",
            "",
            "The canonical data file is [`data/papers.json`](data/papers.json). Each entry keeps "
            "the full paper title, method name, venue, year, method category, method "
            "subcategory, and links.",
            "",
            "```json",
            "{",
            '  "method_name": "DeepMimic",',
            '  "title": "DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills",',
            '  "year": 2018,',
            '  "venue": "SIGGRAPH",',
            '  "primary_category": "motion-retargeting-and-tracking",',
            '  "subcategory": "physics-based-motion-tracking",',
            '  "links": {"paper": "https://doi.org/10.1145/3197517.3201311", "code": "", "project": ""}',
            "}",
            "```",
            "",
            "## Citation",
            "",
            "If you use this list, please cite the survey paper. A formal BibTeX entry can be "
            "added once the final publication metadata is available.",
        ]
    )

    README_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
