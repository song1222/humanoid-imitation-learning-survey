# Contributing

Contributions should preserve the survey taxonomy instead of turning the repository into a flat paper dump.

## Add a Paper

1. Open `data/papers.json`.
2. Add one entry to the `papers` array.
3. Fill both `method_name` and the full article `title`.
4. Add `links.paper` whenever a paper page, DOI, OpenReview, CVF, or arXiv URL is available.
5. Choose exactly one `primary_category`.
6. Add all secondary information as metadata.
7. Run:

```bash
python scripts/generate_readme.py
python scripts/validate_papers.py
```

## Primary Category Rules

- `motion-retargeting-and-tracking`: the main contribution is transferring, retargeting, or physically tracking reference motion.
- `skill-acquisition`: the main contribution is acquiring a concrete task skill such as sports, acrobatics, recovery, or long-horizon behavior.
- `interaction-learning`: the main contribution is object, scene, or human interaction.
- `generalist-humanoid-policies`: the main contribution is a broad policy, behavior foundation model, VLA-style model, or multi-skill generalist controller.

## Metadata Rules

- Use `data_sources` for MoCap, Video, Learned Motion Priors, Teleoperation, or Unspecified.
- Use `platforms` for simulators or real robot platforms.
- Use `tags` for secondary mechanisms such as diffusion, teacher-student distillation, adversarial imitation, language conditioning, or sim-to-real.
- Use `method_name` for the short method name and `title` for the full article title.
- Use `links.paper`, `links.project`, and `links.code` so the README can work like an awesome-list.
- Use `notes` only for short clarifications.

## Avoid

- Duplicating the same paper into multiple primary categories.
- Classifying by model backbone when the paper's contribution is really a data-flow or deployment pipeline.
- Adding papers that only mention humanoids in related work.
- Replacing a full paper title with only an acronym unless the full title is still unknown and the entry has a note.
