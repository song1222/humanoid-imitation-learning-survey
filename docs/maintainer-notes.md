# Maintainer Notes

## Main Design Choice

The repository mirrors the survey's data-method-evaluation pipeline:

1. Data Sources
2. Methods of Humanoid Imitation Learning
3. Evaluation Metrics and Platforms

The method taxonomy used by the representative-methods table is:

1. Motion Retargeting and Tracking
2. Skill Acquisition
3. Interaction Learning
4. Generalist Humanoid Policies

The README therefore provides a Data Sources index, a Method Taxonomy list, and an Evaluation summary. Simulator, robot, language, vision, teacher-student training, and sim-to-real information should remain metadata unless the survey adds them as explicit categories.

## Why Not Multi-Folder Duplication

Many humanoid imitation papers combine several ingredients. A paper may use human MoCap, a retargeting pipeline, an RL teacher, behavior cloning, and real-robot deployment. Duplicating such a paper across every possible category makes the repository hard to maintain.

Instead:

- `primary_category` records the paper's method category from the survey table.
- `data_sources` records where the supervision comes from and drives the Data Sources index.
- `platforms` records simulator or hardware.
- `tags` records secondary mechanisms.
- `notes` records short classification caveats.

## Category Boundary Checks

- Put a paper in `motion-retargeting-and-tracking` when the contribution is motion transfer, retargeting, reference tracking, or physically executable imitation.
- Put a paper in `skill-acquisition` when the contribution is a concrete behavior family such as sports, acrobatics, or long-horizon skills.
- Put a paper in `interaction-learning` when object, scene, or human interaction is central.
- Put a paper in `generalist-humanoid-policies` when the contribution is broad behavioral coverage, multi-skill policy reuse, promptable control, or VLA-style generalization.

When uncertain, classify by the main claim and use metadata for the rest.
