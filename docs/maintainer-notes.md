# Maintainer Notes

## Main Design Choice

The repository uses the survey's method taxonomy as the primary browsing axis:

1. Motion Retargeting and Tracking
2. Skill Acquisition
3. Interaction Learning
4. Generalist Humanoid Policies

This keeps the repository easy to browse. Data source, simulator, robot, language, vision, teacher-student training, and sim-to-real information should be metadata, not competing top-level folders.

## Why Not Multi-Folder Duplication

Many humanoid imitation papers combine several ingredients. A paper may use human MoCap, a retargeting pipeline, an RL teacher, behavior cloning, and real-robot deployment. Duplicating such a paper across every possible category makes the repository hard to maintain.

Instead:

- `primary_category` records the paper's main contribution.
- `data_sources` records where the supervision comes from.
- `platforms` records simulator or hardware.
- `tags` records secondary mechanisms.
- `notes` records short classification caveats.

## Category Boundary Checks

- Put a paper in `motion-retargeting-and-tracking` when the contribution is motion transfer, retargeting, reference tracking, or physically executable imitation.
- Put a paper in `skill-acquisition` when the contribution is a concrete behavior family such as sports, acrobatics, or long-horizon skills.
- Put a paper in `interaction-learning` when object, scene, or human interaction is central.
- Put a paper in `generalist-humanoid-policies` when the contribution is broad behavioral coverage, multi-skill policy reuse, promptable control, or VLA-style generalization.

When uncertain, classify by the main claim and use metadata for the rest.
