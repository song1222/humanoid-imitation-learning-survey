# Humanoid Imitation Learning Survey

This repository organizes papers from **A Survey of Humanoid Imitation Learning** using the taxonomy defined in the survey.

The repository is built around one main browsing axis:

> How does a method turn demonstrations or motion priors into executable humanoid behavior?

Each paper is assigned to one primary method category. Cross-cutting information such as data source, simulator, robot platform, and evaluation focus is stored as metadata in `data/papers.json`.

## Taxonomy

### Primary method categories

| Category | Count | Scope |
| --- | ---: | --- |
| Motion Retargeting and Tracking | 15 | Human-to-robot motion transfer, retargeting, and physics-based reference tracking. |
| Skill Acquisition | 9 | Task-oriented skills such as sports, acrobatics, and long-horizon behaviors. |
| Interaction Learning | 10 | Object, scene, and human interaction behaviors. |
| Generalist Humanoid Policies | 11 | Scalable policies that unify skills, tasks, language, vision, or foundation-model style behavior priors. |

### Data-source tags

- Data from Humans
  - MoCap
  - Video
- Learned Motion Priors
- Teleoperation
- Unspecified

### Evaluation metadata

Evaluation metadata follows the survey's evaluation section:

- Motion Fidelity Metrics
- Physical Feasibility Metrics
- Task Performance Metrics
- Sim-to-Real Metrics
- Evaluation Tasks
- Simulation Platforms
- Real-World Deployment

## Papers

The canonical paper list is `data/papers.json`.

### Motion Retargeting and Tracking

DeepMimic, SFV, NPMP, AMP, ASE, ControlVAE, PHC, CALM, PDP, TWIST, Diffuse-CLoC, PvP, Any2Track, OmniRetarget, AdaMimic

### Skill Acquisition

RFC, DanceHAT, InsActor, Tennis Skills, KungfuBot, PARC, Learning to Ball, CRISP, Dribble Master

### Interaction Learning

InterPhys, OmniH2O, UniHSI, XGB, InterMimic, TokenHSI, AMO, Beyond Mimicry, VIRAL, HAIC

### Generalist Humanoid Policies

MHC, HumanPlus, HumanVLA, MaskedMimic, SkillMimic, CLoSD, SENTINEL, BiBo, ExBody2, DreamControl, HumanoidExo

## Repository Layout

```text
.
|-- README.md
|-- CONTRIBUTING.md
|-- data/
|   |-- papers.json
|   `-- taxonomy.json
|-- docs/
|   |-- maintainer-notes.md
|   `-- paper-entry-template.md
|-- scripts/
|   `-- validate_papers.py
`-- .github/
    |-- ISSUE_TEMPLATE/
    |   `-- add-paper.yml
    `-- workflows/
        `-- validate.yml
```

## Maintaining the List

1. Add or edit entries in `data/papers.json`.
2. Keep exactly one `primary_category` per paper.
3. Put overlap in `data_sources`, `tags`, `platforms`, and `notes`.
4. Validate the data:

```bash
python scripts/validate_papers.py
```

## Classification Rule

Use the paper's dominant contribution as the primary category. For example, if a system uses MoCap, an RL teacher, and behavior cloning, do not duplicate it across all of those ideas. Assign the primary category by the paper's main role in the humanoid imitation pipeline, then record the rest as metadata.

## Citation

If you use this list, please cite the survey paper. A formal BibTeX entry can be added once the final publication metadata is available.
