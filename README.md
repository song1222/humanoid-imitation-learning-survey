# Awesome Humanoid Imitation Learning Survey

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

This repository collects papers from **A Survey of Humanoid Imitation Learning** and organizes them with the taxonomy used in the survey.

Different from a general humanoid-robot-learning list, this repository mirrors the survey's **data-method-evaluation** pipeline. Papers can be browsed by data source and by the method taxonomy, while simulator, robot platform, project links, and code links are stored as metadata in `data/papers.json`.

## Contents

- [Data Sources](#data-sources)
- [Methods of Humanoid Imitation Learning](#methods-of-humanoid-imitation-learning)
- [Evaluation Metrics and Platforms](#evaluation-metrics-and-platforms)
- [Data Format](#data-format)
- [Contributing](#contributing)

---

## Data Sources

This section follows the survey's data-source taxonomy. Papers with multiple data sources appear in multiple data-source subsections.

### Data from Humans: Motion Capture

High-fidelity human motion demonstrations recorded by optical or inertial motion capture systems.

- [SIGGRAPH 2018](https://doi.org/10.1145/3197517.3201311), **DeepMimic**: DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills (`MoCap`; `Bullet`)
- [ICLR 2019](https://openreview.net/forum?id=BJl6TjRcY7), **NPMP**: Neural Probabilistic Motor Primitives for Humanoid Control (`MoCap`; `MuJoCo`)
- [NIPS 2020](https://proceedings.neurips.cc/paper/2020/hash/f76a89f0cb91bc419542ce9fa43902dc-Abstract.html), **RFC**: Residual Force Control for Agile Human Behavior Imitation and Extended Motion Synthesis (`MoCap`; `MuJoCo`)
- [SIGGRAPH 2021](https://doi.org/10.1145/3450626.3459670), **AMP**: AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control (`MoCap`; `Bullet`)
- ICRA 2022, **DanceHAT**: DanceHAT (`MoCap`; `NAO`)
- [SIGGRAPH 2022](https://doi.org/10.1145/3528223.3530110), **ASE**: ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters (`MoCap`; `Isaac Gym`)
- [SIGGRAPH Asia 2022](https://doi.org/10.1145/3550454.3555434), **ControlVAE**: ControlVAE: Model-Based Learning of Generative Controllers for Physics-Based Characters (`MoCap`; `ODE`)
- [ICCV 2023](https://doi.org/10.1109/ICCV51070.2023.01000), **PHC**: Perpetual Humanoid Control for Real-Time Simulated Avatars (`MoCap`; `Isaac Gym`)
- [NIPS 2023](https://arxiv.org/abs/2312.17135), **InsActor**: InsActor: Instruction-Driven Physics-Based Characters (`MoCap`; `Brax`)
- [SIGGRAPH 2023](https://doi.org/10.1145/3588432.3591541), **CALM**: CALM: Conditional Adversarial Latent Models for Directable Virtual Characters (`MoCap`; `Isaac Gym`)
- SIGGRAPH 2023, **InterPhys**: InterPhys (`MoCap`; `Isaac Gym`)
- [SIGGRAPH 2023](https://doi.org/10.1145/3592408), **Tennis Skills**: Learning Physically Simulated Tennis Skills from Broadcast Videos (`MoCap, Video`; `Isaac Gym`)
- [CoRL 2024](https://proceedings.mlr.press/v270/fu25a.html), **HumanPlus**: HumanPlus: Humanoid Shadowing and Imitation from Humans, [website](https://humanoid-ai.github.io/) / [code](https://github.com/MarkFzp/humanplus) (`MoCap, Teleoperation`; `Unitree H1`)
- [CoRL 2024](https://proceedings.mlr.press/v270/he25b.html), **OmniH2O**: OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning, [website](https://omni.human2humanoid.com/) / [code](https://github.com/LeCAR-Lab/human2humanoid) (`MoCap, Teleoperation`; `Unitree H1`)
- [ECCV 2024](https://arxiv.org/abs/2502.05641), **MHC**: Generating Physically Realistic and Directable Human Motions from Multi-Modal Inputs, [website](https://masked-humanoid.github.io/mhc/) (`MoCap`; `Isaac Gym`)
- [ICLR 2024](https://arxiv.org/abs/2309.07918), **UniHSI**: Unified Human-Scene Interaction via Prompted Chain-of-Contacts, [website](https://github.com/OpenRobotLab/UniHSI) (`MoCap`; `Isaac Gym`)
- [NIPS 2024](https://arxiv.org/abs/2502.14795), **HumanVLA**: Humanoid-VLA: Towards Universal Humanoid Control with Visual Integration (`MoCap`; `Isaac Gym`)
- [SIGGRAPH Asia 2024](https://doi.org/10.1145/3687951), **MaskedMimic**: MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting (`MoCap`; `Isaac Gym`)
- [SIGGRAPH Asia 2024](https://doi.org/10.1145/3680528.3687683), **PDP**: PDP: Physics-Based Character Animation via Diffusion Policy (`MoCap`; `MuJoCo`)
- [CVPR 2025](https://arxiv.org/abs/2502.20390), **InterMimic**: InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions (`MoCap`; `Isaac Gym`)
- [CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_SkillMimic_Learning_Basketball_Interaction_Skills_from_Demonstrations_CVPR_2025_paper.html), **SkillMimic**: SkillMimic: Learning Basketball Interaction Skills from Demonstrations (`MoCap, Video`; `Isaac Gym`)
- [CVPR 2025](https://arxiv.org/abs/2503.19901), **TokenHSI**: TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization, [website](https://liangpan99.github.io/TokenHSI/) (`MoCap`; `Isaac Gym`)
- [CoRL 2025](https://arxiv.org/abs/2505.02833), **TWIST**: TWIST: Teleoperated Whole-Body Imitation System (`MoCap`; `Unitree G1`)
- [NIPS 2025](https://arxiv.org/abs/2506.12851), **KungfuBot**: KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills, [website](https://kungfu-bot.github.io/) (`MoCap, Video`; `Unitree G1`)
- [RSS 2025](https://arxiv.org/abs/2505.03738), **AMO**: AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control, [website](https://amo-humanoid.github.io/) (`MoCap`; `Unitree G1`)
- [SIGGRAPH 2025](https://doi.org/10.1145/3731206), **Diffuse-CLoC**: Diffuse-CLoC: Guided Diffusion for Physics-Based Character Look-Ahead Control (`MoCap`; `Isaac Gym`)
- [SIGGRAPH Asia 2025](https://doi.org/10.1145/3763367), **Learning to Ball**: Learning to Ball: Composing Policies for Long-Horizon Basketball Moves (`MoCap, Video`; `Isaac Gym`)
- [AAAI 2026](https://arxiv.org/abs/2509.13833), **Any2Track**: Track Any Motions under Any Disturbances, [website](https://zzk273.github.io/Any2Track/) (`MoCap`; `Unitree G1`)
- [CVPR 2026](https://arxiv.org/abs/2508.08241), **Beyond Mimicry**: BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion (`MoCap`; `Unitree G1`)
- [CVPR 2026](https://arxiv.org/abs/2512.13093), **PvP**: PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations (`MoCap`; `LimX Oli`)
- [CVPR 2026](https://arxiv.org/abs/2511.19236), **SENTINEL**: SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control (`MoCap`; `Unitree G1`)
- ICLR 2026, **BiBo**: BiBo (`MoCap`; `Isaac Gym`)
- [ICLR 2026](https://arxiv.org/abs/2412.13196), **ExBody2**: ExBody2: Advanced Expressive Humanoid Whole-Body Control, [website](https://exbody2.github.io/) (`MoCap`; `Unitree G1`)
- [ICRA 2026](https://arxiv.org/abs/2509.26633), **OmniRetarget**: OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction, [website](https://omniretarget.github.io/) (`MoCap`; `Unitree G1`)
- [RSS 2026](https://arxiv.org/abs/2602.11758), **HAIC**: HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model, [website](https://haic-humanoid.github.io/) (`MoCap`; `Unitree G1`)

### Data from Humans: Video-based Reconstruction

Human demonstrations reconstructed from monocular, broadcast, Internet, or other video sources.

- [SIGGRAPH Asia 2018](https://arxiv.org/abs/1810.03599), **SFV**: SFV: Reinforcement Learning of Physical Skills from Videos (`Video`; `Bullet`)
- [SIGGRAPH 2023](https://doi.org/10.1145/3592408), **Tennis Skills**: Learning Physically Simulated Tennis Skills from Broadcast Videos (`MoCap, Video`; `Isaac Gym`)
- [CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_SkillMimic_Learning_Basketball_Interaction_Skills_from_Demonstrations_CVPR_2025_paper.html), **SkillMimic**: SkillMimic: Learning Basketball Interaction Skills from Demonstrations (`MoCap, Video`; `Isaac Gym`)
- [NIPS 2025](https://arxiv.org/abs/2506.12851), **KungfuBot**: KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills, [website](https://kungfu-bot.github.io/) (`MoCap, Video`; `Unitree G1`)
- [SIGGRAPH Asia 2025](https://doi.org/10.1145/3763367), **Learning to Ball**: Learning to Ball: Composing Policies for Long-Horizon Basketball Moves (`MoCap, Video`; `Isaac Gym`)
- [ICLR 2026](https://arxiv.org/abs/2512.14696), **CRISP**: CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives (`Video`; `Isaac Gym`)
- [ICRA 2026](https://arxiv.org/abs/2510.14454), **AdaMimic**: AdaMimic: Towards Adaptable Humanoid Control via Adaptive Motion Tracking, [website](https://taohuang13.github.io/adamimic.github.io/) (`Video`; `Unitree G1`)

### Data from Learned Motion Priors

Generated or synthesized motions from learned behavior or motion-generation models.

- [ICLR 2025](https://openreview.net/forum?id=pZISppZSTv), **CLoSD**: CLoSD: Closing the Loop between Simulation and Diffusion for Multi-Task Character Control (`Learned Motion Priors`; `Isaac Gym`)
- [SIGGRAPH 2025](https://doi.org/10.1145/3721238.3730616), **PARC**: PARC: Physics-Based Augmentation with Reinforcement Learning for Character Controllers (`Learned Motion Priors`; `Isaac Gym`)
- [ICRA 2026](https://arxiv.org/abs/2509.14353), **DreamControl**: DreamControl: Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion (`Learned Motion Priors`; `Unitree G1`)

### Data from Teleoperation

Robot embodiment-specific demonstrations collected through humanoid teleoperation.

- [CoRL 2024](https://proceedings.mlr.press/v270/fu25a.html), **HumanPlus**: HumanPlus: Humanoid Shadowing and Imitation from Humans, [website](https://humanoid-ai.github.io/) / [code](https://github.com/MarkFzp/humanplus) (`MoCap, Teleoperation`; `Unitree H1`)
- [CoRL 2024](https://proceedings.mlr.press/v270/he25b.html), **OmniH2O**: OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning, [website](https://omni.human2humanoid.com/) / [code](https://github.com/LeCAR-Lab/human2humanoid) (`MoCap, Teleoperation`; `Unitree H1`)
- [RAL 2024](https://doi.org/10.1109/LRA.2024.3495577), **XGB**: XBG: End-to-End Imitation Learning for Autonomous Behaviour in Human-Robot Interaction and Collaboration (`Teleoperation`; `ErgoCub`)
- [CVPR 2026](https://arxiv.org/abs/2511.15200), **VIRAL**: VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation (`Teleoperation`; `Unitree G1`)
- [ICRA 2026](https://arxiv.org/abs/2510.03022), **HumanoidExo**: HumanoidExo: Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton, [website](https://humanoid-exo.github.io/) (`Teleoperation`; `Unitree G1`)

### Unspecified Data Source

The survey table does not specify a data source for this entry.

- [ICRA 2026](https://arxiv.org/abs/2505.12679), **Dribble Master**: Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion (`Unspecified`; `Booster T1`)

## Methods of Humanoid Imitation Learning

This section follows the survey's method taxonomy and the representative-methods table.

### Motion Retargeting and Tracking

Human-to-robot motion transfer, retargeting, and physics-based reference tracking.

- [SIGGRAPH 2018](https://doi.org/10.1145/3197517.3201311), **DeepMimic**: DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills (`MoCap`; `Bullet`)
- [SIGGRAPH Asia 2018](https://arxiv.org/abs/1810.03599), **SFV**: SFV: Reinforcement Learning of Physical Skills from Videos (`Video`; `Bullet`)
- [ICLR 2019](https://openreview.net/forum?id=BJl6TjRcY7), **NPMP**: Neural Probabilistic Motor Primitives for Humanoid Control (`MoCap`; `MuJoCo`)
- [SIGGRAPH 2021](https://doi.org/10.1145/3450626.3459670), **AMP**: AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control (`MoCap`; `Bullet`)
- [SIGGRAPH 2022](https://doi.org/10.1145/3528223.3530110), **ASE**: ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters (`MoCap`; `Isaac Gym`)
- [SIGGRAPH Asia 2022](https://doi.org/10.1145/3550454.3555434), **ControlVAE**: ControlVAE: Model-Based Learning of Generative Controllers for Physics-Based Characters (`MoCap`; `ODE`)
- [ICCV 2023](https://doi.org/10.1109/ICCV51070.2023.01000), **PHC**: Perpetual Humanoid Control for Real-Time Simulated Avatars (`MoCap`; `Isaac Gym`)
- [SIGGRAPH 2023](https://doi.org/10.1145/3588432.3591541), **CALM**: CALM: Conditional Adversarial Latent Models for Directable Virtual Characters (`MoCap`; `Isaac Gym`)
- [SIGGRAPH Asia 2024](https://doi.org/10.1145/3680528.3687683), **PDP**: PDP: Physics-Based Character Animation via Diffusion Policy (`MoCap`; `MuJoCo`)
- [CoRL 2025](https://arxiv.org/abs/2505.02833), **TWIST**: TWIST: Teleoperated Whole-Body Imitation System (`MoCap`; `Unitree G1`)
- [SIGGRAPH 2025](https://doi.org/10.1145/3731206), **Diffuse-CLoC**: Diffuse-CLoC: Guided Diffusion for Physics-Based Character Look-Ahead Control (`MoCap`; `Isaac Gym`)
- [AAAI 2026](https://arxiv.org/abs/2509.13833), **Any2Track**: Track Any Motions under Any Disturbances, [website](https://zzk273.github.io/Any2Track/) (`MoCap`; `Unitree G1`)
- [CVPR 2026](https://arxiv.org/abs/2512.13093), **PvP**: PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations (`MoCap`; `LimX Oli`)
- [ICRA 2026](https://arxiv.org/abs/2510.14454), **AdaMimic**: AdaMimic: Towards Adaptable Humanoid Control via Adaptive Motion Tracking, [website](https://taohuang13.github.io/adamimic.github.io/) (`Video`; `Unitree G1`)
- [ICRA 2026](https://arxiv.org/abs/2509.26633), **OmniRetarget**: OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction, [website](https://omniretarget.github.io/) (`MoCap`; `Unitree G1`)

### Skill Acquisition

Task-oriented humanoid skills such as sports, acrobatics, and long-horizon behavior.

- [NIPS 2020](https://proceedings.neurips.cc/paper/2020/hash/f76a89f0cb91bc419542ce9fa43902dc-Abstract.html), **RFC**: Residual Force Control for Agile Human Behavior Imitation and Extended Motion Synthesis (`MoCap`; `MuJoCo`)
- ICRA 2022, **DanceHAT**: DanceHAT (`MoCap`; `NAO`)
- [NIPS 2023](https://arxiv.org/abs/2312.17135), **InsActor**: InsActor: Instruction-Driven Physics-Based Characters (`MoCap`; `Brax`)
- [SIGGRAPH 2023](https://doi.org/10.1145/3592408), **Tennis Skills**: Learning Physically Simulated Tennis Skills from Broadcast Videos (`MoCap, Video`; `Isaac Gym`)
- [NIPS 2025](https://arxiv.org/abs/2506.12851), **KungfuBot**: KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills, [website](https://kungfu-bot.github.io/) (`MoCap, Video`; `Unitree G1`)
- [SIGGRAPH 2025](https://doi.org/10.1145/3721238.3730616), **PARC**: PARC: Physics-Based Augmentation with Reinforcement Learning for Character Controllers (`Learned Motion Priors`; `Isaac Gym`)
- [SIGGRAPH Asia 2025](https://doi.org/10.1145/3763367), **Learning to Ball**: Learning to Ball: Composing Policies for Long-Horizon Basketball Moves (`MoCap, Video`; `Isaac Gym`)
- [ICLR 2026](https://arxiv.org/abs/2512.14696), **CRISP**: CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives (`Video`; `Isaac Gym`)
- [ICRA 2026](https://arxiv.org/abs/2505.12679), **Dribble Master**: Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion (`Unspecified`; `Booster T1`)

### Interaction Learning

Object, scene, and human interaction behaviors.

- SIGGRAPH 2023, **InterPhys**: InterPhys (`MoCap`; `Isaac Gym`)
- [CoRL 2024](https://proceedings.mlr.press/v270/he25b.html), **OmniH2O**: OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning, [website](https://omni.human2humanoid.com/) / [code](https://github.com/LeCAR-Lab/human2humanoid) (`MoCap, Teleoperation`; `Unitree H1`)
- [ICLR 2024](https://arxiv.org/abs/2309.07918), **UniHSI**: Unified Human-Scene Interaction via Prompted Chain-of-Contacts, [website](https://github.com/OpenRobotLab/UniHSI) (`MoCap`; `Isaac Gym`)
- [RAL 2024](https://doi.org/10.1109/LRA.2024.3495577), **XGB**: XBG: End-to-End Imitation Learning for Autonomous Behaviour in Human-Robot Interaction and Collaboration (`Teleoperation`; `ErgoCub`)
- [CVPR 2025](https://arxiv.org/abs/2502.20390), **InterMimic**: InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions (`MoCap`; `Isaac Gym`)
- [CVPR 2025](https://arxiv.org/abs/2503.19901), **TokenHSI**: TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization, [website](https://liangpan99.github.io/TokenHSI/) (`MoCap`; `Isaac Gym`)
- [RSS 2025](https://arxiv.org/abs/2505.03738), **AMO**: AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control, [website](https://amo-humanoid.github.io/) (`MoCap`; `Unitree G1`)
- [CVPR 2026](https://arxiv.org/abs/2508.08241), **Beyond Mimicry**: BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion (`MoCap`; `Unitree G1`)
- [CVPR 2026](https://arxiv.org/abs/2511.15200), **VIRAL**: VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation (`Teleoperation`; `Unitree G1`)
- [RSS 2026](https://arxiv.org/abs/2602.11758), **HAIC**: HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model, [website](https://haic-humanoid.github.io/) (`MoCap`; `Unitree G1`)

### Generalist Humanoid Policies

Broad-coverage policies, multi-skill controllers, and foundation/VLA-style humanoid policies.

- [CoRL 2024](https://proceedings.mlr.press/v270/fu25a.html), **HumanPlus**: HumanPlus: Humanoid Shadowing and Imitation from Humans, [website](https://humanoid-ai.github.io/) / [code](https://github.com/MarkFzp/humanplus) (`MoCap, Teleoperation`; `Unitree H1`)
- [ECCV 2024](https://arxiv.org/abs/2502.05641), **MHC**: Generating Physically Realistic and Directable Human Motions from Multi-Modal Inputs, [website](https://masked-humanoid.github.io/mhc/) (`MoCap`; `Isaac Gym`)
- [NIPS 2024](https://arxiv.org/abs/2502.14795), **HumanVLA**: Humanoid-VLA: Towards Universal Humanoid Control with Visual Integration (`MoCap`; `Isaac Gym`)
- [SIGGRAPH Asia 2024](https://doi.org/10.1145/3687951), **MaskedMimic**: MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting (`MoCap`; `Isaac Gym`)
- [CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_SkillMimic_Learning_Basketball_Interaction_Skills_from_Demonstrations_CVPR_2025_paper.html), **SkillMimic**: SkillMimic: Learning Basketball Interaction Skills from Demonstrations (`MoCap, Video`; `Isaac Gym`)
- [ICLR 2025](https://openreview.net/forum?id=pZISppZSTv), **CLoSD**: CLoSD: Closing the Loop between Simulation and Diffusion for Multi-Task Character Control (`Learned Motion Priors`; `Isaac Gym`)
- [CVPR 2026](https://arxiv.org/abs/2511.19236), **SENTINEL**: SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control (`MoCap`; `Unitree G1`)
- ICLR 2026, **BiBo**: BiBo (`MoCap`; `Isaac Gym`)
- [ICLR 2026](https://arxiv.org/abs/2412.13196), **ExBody2**: ExBody2: Advanced Expressive Humanoid Whole-Body Control, [website](https://exbody2.github.io/) (`MoCap`; `Unitree G1`)
- [ICRA 2026](https://arxiv.org/abs/2509.14353), **DreamControl**: DreamControl: Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion (`Learned Motion Priors`; `Unitree G1`)
- [ICRA 2026](https://arxiv.org/abs/2510.03022), **HumanoidExo**: HumanoidExo: Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton, [website](https://humanoid-exo.github.io/) (`Teleoperation`; `Unitree G1`)

## Evaluation Metrics and Platforms

### Evaluation Metrics

- Motion Fidelity Metrics: position, orientation, velocity/acceleration, and distribution similarity.
- Physical Feasibility Metrics: energy, contact quality, and stability.
- Task Performance Metrics: success rate, survival time, and task duration.
- Sim-to-Real Metrics: zero-shot transfer, robustness, and sim-to-real gap.

### Evaluation Tasks

- Locomotion
- Stationary Manipulation
- Loco-Manipulation
- Scene Interaction
- Human-Human Interaction
- Open-World Embodied Tasks

### Simulation Platforms and Real-World Deployment

- Physical simulation platforms: Isaac and MuJoCo.
- Real-world deployment: Unitree humanoid platforms, Booster humanoid platforms, and large-scale sim-to-real evaluation.

## Data Format

The canonical data file is [`data/papers.json`](data/papers.json). Each entry keeps the full paper title, method name, venue, year, data source, method category, platform, and links.

```json
{
  "method_name": "DeepMimic",
  "title": "DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills",
  "year": 2018,
  "venue": "SIGGRAPH",
  "data_sources": ["MoCap"],
  "primary_category": "motion-retargeting-and-tracking",
  "platforms": ["Bullet"],
  "links": {"paper": "https://doi.org/10.1145/3197517.3201311", "code": "", "project": ""}
}
```

## Contributing

Please keep exactly one `primary_category` per paper. If a paper spans multiple ideas, put the overlap in `data_sources`, `tags`, `platforms`, `links`, and `notes`.

After editing `data/papers.json`, regenerate and validate the list:

```bash
python scripts/generate_readme.py
python scripts/validate_papers.py
```

## Citation

If you use this list, please cite the survey paper. A formal BibTeX entry can be added once the final publication metadata is available.
