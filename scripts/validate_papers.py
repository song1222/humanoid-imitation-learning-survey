#!/usr/bin/env python3
"""Validate the repository paper metadata."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPERS_PATH = ROOT / "data" / "papers.json"
TAXONOMY_PATH = ROOT / "data" / "taxonomy.json"

REQUIRED_FIELDS = {
    "id",
    "method_name",
    "title",
    "bib_key",
    "year",
    "venue",
    "data_sources",
    "primary_category",
    "platforms",
    "tags",
    "links",
    "notes",
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    taxonomy = load_json(TAXONOMY_PATH)
    papers_doc = load_json(PAPERS_PATH)

    allowed_categories = {item["id"] for item in taxonomy["primary_categories"]}
    allowed_data_sources = {item["name"] for item in taxonomy["data_sources"]}
    papers = papers_doc.get("papers", [])

    errors: list[str] = []
    ids: set[str] = set()
    category_counts: Counter[str] = Counter()

    for index, paper in enumerate(papers, start=1):
        label = paper.get("id", f"entry-{index}")
        missing = REQUIRED_FIELDS - set(paper)
        if missing:
            errors.append(f"{label}: missing fields: {', '.join(sorted(missing))}")

        paper_id = paper.get("id")
        if not isinstance(paper_id, str) or not paper_id:
            errors.append(f"entry {index}: id must be a non-empty string")
        elif paper_id in ids:
            errors.append(f"{paper_id}: duplicate id")
        else:
            ids.add(paper_id)

        if not isinstance(paper.get("year"), int):
            errors.append(f"{label}: year must be an integer")

        for text_field in ("method_name", "title", "venue", "bib_key", "notes"):
            if not isinstance(paper.get(text_field), str):
                errors.append(f"{label}: {text_field} must be a string")

        if paper.get("title") == paper.get("method_name") and not paper.get("notes"):
            errors.append(
                f"{label}: title still looks like a method name; add a full title or a note"
            )

        category = paper.get("primary_category")
        if category not in allowed_categories:
            errors.append(f"{label}: unknown primary_category: {category}")
        else:
            category_counts[category] += 1

        data_sources = paper.get("data_sources")
        if not isinstance(data_sources, list) or not data_sources:
            errors.append(f"{label}: data_sources must be a non-empty list")
        else:
            for source in data_sources:
                if source not in allowed_data_sources:
                    errors.append(f"{label}: unknown data source: {source}")

        platforms = paper.get("platforms")
        if not isinstance(platforms, list) or not platforms:
            errors.append(f"{label}: platforms must be a non-empty list")

        tags = paper.get("tags")
        if not isinstance(tags, list):
            errors.append(f"{label}: tags must be a list")

        links = paper.get("links")
        if not isinstance(links, dict):
            errors.append(f"{label}: links must be an object")
        else:
            for key in ("paper", "code", "project"):
                if key not in links:
                    errors.append(f"{label}: links missing {key}")

    if errors:
        print("Metadata validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: {len(papers)} papers")
    for category in sorted(category_counts):
        print(f"- {category}: {category_counts[category]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
