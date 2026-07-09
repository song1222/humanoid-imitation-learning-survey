# Paper Entry Template

Copy this object into `data/papers.json` and fill in the fields.

```json
{
  "id": "short-lowercase-id",
  "title": "Paper or method name",
  "year": 2026,
  "venue": "Conference or journal",
  "data_sources": ["MoCap"],
  "primary_category": "motion-retargeting-and-tracking",
  "platforms": ["Isaac Gym"],
  "tags": ["representative-method"],
  "links": {
    "paper": "",
    "code": "",
    "project": ""
  },
  "notes": ""
}
```

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
