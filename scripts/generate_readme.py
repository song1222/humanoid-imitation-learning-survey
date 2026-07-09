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
        "Human-to-robot motion transfer, retargeting, and physics-based reference tracking."
    ),
    "skill-acquisition": (
        "Task-oriented humanoid skills such as sports, acrobatics, and long-horizon behavior."
    ),
    "interaction-learning": "Object, scene, and human interaction behaviors.",
    "generalist-humanoid-policies": (
        "Broad-coverage policies, multi-skill controllers, and foundation/VLA-style humanoid policies."
    ),
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

    data_sources = ", ".join(paper.get("data_sources", []))
    platforms = ", ".join(paper.get("platforms", []))
    meta = f"`{data_sources}`; `{platforms}`"
    suffix = f", {' / '.join(extras)}" if extras else ""
    return f"- {venue_part}, **{method}**: {title}{suffix} ({meta})"


def main() -> int:
    data = json.loads(PAPERS_PATH.read_text(encoding="utf-8"))

    lines = [
        "# Awesome Humanoid Imitation Learning Survey",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) "
        "[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]"
        "(http://makeapullrequest.com)",
        "",
        "This repository collects papers from **A Survey of Humanoid Imitation Learning** "
        "and organizes them with the taxonomy used in the survey.",
        "",
        "Different from a general humanoid-robot-learning list, this repository keeps one main "
        "classification line: **how a method turns demonstrations or motion priors into "
        "executable humanoid behavior**. Data source, simulator, robot platform, project links, "
        "and code links are stored as metadata in `data/papers.json`.",
        "",
        "## Contents",
        "",
    ]

    for _, name in CATEGORY_ORDER:
        anchor = name.lower().replace(" ", "-")
        lines.append(f"- [{name}](#{anchor})")
    lines.extend(["- [Data Format](#data-format)", "- [Contributing](#contributing)", "", "---", ""])

    for category_id, category_name in CATEGORY_ORDER:
        papers = [p for p in data["papers"] if p["primary_category"] == category_id]
        lines.extend([f"## {category_name}", "", CATEGORY_SCOPE[category_id], ""])
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
            "the full paper title, method name, venue, year, data source, primary category, "
            "platform, and links.",
            "",
            "```json",
            "{",
            '  "method_name": "DeepMimic",',
            '  "title": "DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills",',
            '  "year": 2018,',
            '  "venue": "SIGGRAPH",',
            '  "data_sources": ["MoCap"],',
            '  "primary_category": "motion-retargeting-and-tracking",',
            '  "platforms": ["Bullet"],',
            '  "links": {"paper": "https://doi.org/10.1145/3197517.3201311", "code": "", "project": ""}',
            "}",
            "```",
            "",
            "## Contributing",
            "",
            "Please keep exactly one `primary_category` per paper. If a paper spans multiple ideas, "
            "put the overlap in `data_sources`, `tags`, `platforms`, `links`, and `notes`.",
            "",
            "After editing `data/papers.json`, regenerate and validate the list:",
            "",
            "```bash",
            "python scripts/generate_readme.py",
            "python scripts/validate_papers.py",
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
