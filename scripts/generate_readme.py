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

DATA_SOURCE_ORDER = [
    ("MoCap", "Motion Capture", "Data from Humans"),
    ("Video", "Video-based Reconstruction", "Data from Humans"),
    ("Learned Motion Priors", "Data from Learned Motion Priors", ""),
    ("Teleoperation", "Data from Teleoperation", ""),
    ("Unspecified", "Unspecified Data Source", ""),
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

DATA_SOURCE_SCOPE = {
    "MoCap": (
        "High-fidelity human motion demonstrations recorded by optical or inertial motion "
        "capture systems."
    ),
    "Video": (
        "Human demonstrations reconstructed from monocular, broadcast, Internet, or other "
        "video sources."
    ),
    "Learned Motion Priors": (
        "Generated or synthesized motions from learned behavior or motion-generation models."
    ),
    "Teleoperation": (
        "Robot embodiment-specific demonstrations collected through humanoid teleoperation."
    ),
    "Unspecified": "The survey table does not specify a data source for this entry.",
}

EVALUATION_GROUPS = [
    (
        "Evaluation Metrics",
        [
            "Motion Fidelity Metrics: position, orientation, velocity/acceleration, and distribution similarity.",
            "Physical Feasibility Metrics: energy, contact quality, and stability.",
            "Task Performance Metrics: success rate, survival time, and task duration.",
            "Sim-to-Real Metrics: zero-shot transfer, robustness, and sim-to-real gap.",
        ],
    ),
    (
        "Evaluation Tasks",
        [
            "Locomotion",
            "Stationary Manipulation",
            "Loco-Manipulation",
            "Scene Interaction",
            "Human-Human Interaction",
            "Open-World Embodied Tasks",
        ],
    ),
    (
        "Simulation Platforms and Real-World Deployment",
        [
            "Physical simulation platforms: Isaac and MuJoCo.",
            "Real-world deployment: Unitree humanoid platforms, Booster humanoid platforms, and large-scale sim-to-real evaluation.",
        ],
    ),
]


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
        "Different from a general humanoid-robot-learning list, this repository mirrors the "
        "survey's **data-method-evaluation** pipeline. Papers can be browsed by data source "
        "and by the method taxonomy, while simulator, robot platform, project links, and code "
        "links are stored as metadata in `data/papers.json`.",
        "",
        "## Contents",
        "",
        "- [Data Sources](#data-sources)",
        "- [Methods of Humanoid Imitation Learning](#methods-of-humanoid-imitation-learning)",
    ]

    lines.extend(
        [
            "- [Evaluation Metrics and Platforms](#evaluation-metrics-and-platforms)",
            "- [Data Format](#data-format)",
            "- [Contributing](#contributing)",
            "",
            "---",
            "",
            "## Data Sources",
            "",
            "This section follows the survey's data-source taxonomy. Papers with multiple data "
            "sources appear in multiple data-source subsections.",
            "",
        ]
    )

    for source_name, heading, parent in DATA_SOURCE_ORDER:
        papers = [p for p in data["papers"] if source_name in p.get("data_sources", [])]
        if not papers:
            continue
        title = f"{parent}: {heading}" if parent else heading
        lines.extend([f"### {title}", "", DATA_SOURCE_SCOPE[source_name], ""])
        for paper in sorted(
            papers, key=lambda p: (p["year"], p["venue"], p.get("method_name", p["title"]).lower())
        ):
            lines.append(paper_line(paper))
        lines.append("")

    lines.extend(
        [
            "## Methods of Humanoid Imitation Learning",
            "",
            "This section follows the survey's method taxonomy and the representative-methods "
            "table.",
            "",
        ]
    )

    for category_id, category_name in CATEGORY_ORDER:
        papers = [p for p in data["papers"] if p["primary_category"] == category_id]
        lines.extend([f"### {category_name}", "", CATEGORY_SCOPE[category_id], ""])
        for paper in sorted(
            papers, key=lambda p: (p["year"], p["venue"], p.get("method_name", p["title"]).lower())
        ):
            lines.append(paper_line(paper))
        lines.append("")

    lines.extend(["## Evaluation Metrics and Platforms", ""])
    for group_name, items in EVALUATION_GROUPS:
        lines.extend([f"### {group_name}", ""])
        for item in items:
            lines.append(f"- {item}")
        lines.append("")

    lines.extend(
        [
            "## Data Format",
            "",
            "The canonical data file is [`data/papers.json`](data/papers.json). Each entry keeps "
            "the full paper title, method name, venue, year, data source, method category, "
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
