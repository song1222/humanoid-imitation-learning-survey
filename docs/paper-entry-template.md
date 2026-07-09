# Paper Entry Template

Copy this object into `data/papers.json` and fill in the fields.

```json
{
  "id": "short-lowercase-id",
  "method_name": "Short method name",
  "title": "Full Paper Title: Subtitle If Any",
  "bib_key": "BibTeXKey",
  "year": 2026,
  "venue": "Conference or journal",
  "data_sources": ["MoCap"],
  "primary_category": "motion-retargeting-and-tracking",
  "platforms": ["Isaac Gym"],
  "tags": ["representative-method"],
  "links": {
    "paper": "https://arxiv.org/abs/xxxx.xxxxx",
    "code": "https://github.com/owner/repo",
    "project": "https://project-page.example"
  },
  "notes": ""
}
```

Field meanings:

- `method_name`: short name shown in bold, such as `DeepMimic`.
- `title`: full article title.
- `bib_key`: citation key from the survey BibTeX file when available.
- `links.paper`: paper, DOI, OpenReview, CVF, or arXiv page.
- `links.project`: project website.
- `links.code`: code repository.

Allowed `primary_category` values:

- `motion-retargeting-and-tracking`
- `skill-acquisition`
- `interaction-learning`
- `generalist-humanoid-policies`

Allowed `data_sources` values:

- `MoCap`
- `Video`
- `Learned Motion Priors`
- `Teleoperation`
- `Unspecified`
