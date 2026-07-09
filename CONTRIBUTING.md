# Contributing

Contributions should preserve the survey taxonomy instead of turning the repository into a flat paper dump.

## Add a Paper

1. Open `data/papers.json`.
2. Add one entry to the `papers` array.
3. Choose exactly one `primary_category`.
4. Add all secondary information as metadata.
5. Run:

```bash
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
- Use `notes` only for short clarifications.

## Avoid

- Duplicating the same paper into multiple primary categories.
- Classifying by model backbone when the paper's contribution is really a data-flow or deployment pipeline.
- Adding papers that only mention humanoids in related work.
