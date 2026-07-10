# Awesome Humanoid Imitation Learning Survey

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

![Method Taxonomy](assets/years.png)

This repository collects papers from **A Survey of Humanoid Imitation Learning** and organizes them according to the survey's **Methods of Humanoid Imitation Learning** taxonomy.

Data source, simulator, robot platform, project links, and code links are kept as metadata in `data/papers.json`, but the README classification follows only the method categories and subcategories used in the paper.

## Contents

- [Awesome Humanoid Imitation Learning](#awesome-humanoid-imitation-learning)
  - [Motion Retargeting and Tracking](#motion-retargeting-and-tracking)
  - [Skill Acquisition](#skill-acquisition)
  - [Interaction Learning](#interaction-learning)
  - [Generalist Humanoid Policies](#generalist-humanoid-policies)
- [Data Format](#data-format)
- [Contributing](#contributing)

---

## Awesome Humanoid Imitation Learning

### Motion Retargeting and Tracking

Human-to-robot motion transfer, retargeting, and physics-based reference tracking.

#### Motion Retargeting

- [T-RO 2017](https://doi.org/10.1109/TRO.2017.2752711), **Ayusawa et al.**: Motion Retargeting for Humanoid Robots Based on Simultaneous Morphing Parameter Identification and Motion Optimization (`Unspecified`; `Unspecified`)
- [Humanoids 2019](https://doi.org/10.1109/Humanoids43949.2019.9035059), **Whole-Body Geometric Retargeting**: Whole-Body Geometric Retargeting for Humanoid Robots (`Unspecified`; `Unspecified`)
- [ICRA 2021](https://doi.org/10.1109/ICRA48506.2021.9560860), **S3LE**: Self-Supervised Motion Retargeting with Safety Guarantee (`Unspecified`; `Unspecified`)
- [SIGGRAPH Asia 2023](https://doi.org/10.1145/3610548.3618206), **SAME**: SAME: Skeleton-Agnostic Motion Embedding for Character Animation (`Unspecified`; `Unspecified`)
- [arXiv 2025](https://doi.org/10.48550/arXiv.2510.02252), **GMR**: Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking (`Unspecified`; `Unspecified`)
- [ICRA 2026](https://arxiv.org/abs/2509.26633), **OmniRetarget**: OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction, [website](https://omniretarget.github.io/) (`MoCap`; `Unitree G1`)
- arXiv 2026, **Human2Humanoid**: Human2Humanoid: Physics-Aware Cross-Morphology Motion Retargeting for Humanoid Robots (`Unspecified`; `Unspecified`)
- [arXiv 2026](https://doi.org/10.48550/arXiv.2603.22201), **NMR**: Make Tracking Easy: Neural Motion Retargeting for Humanoid Whole-body Control (`Unspecified`; `Unspecified`)

#### Physics-based Motion Tracking

- [CoRL 2017](https://arxiv.org/abs/1703.09327), **DART**: DART: Noise Injection for Robust Imitation Learning (`Unspecified`; `MuJoCo, Toyota HSR`)
- [arXiv 2017](https://arxiv.org/abs/1707.02747), **Robust Imitation**: Robust Imitation of Diverse Behaviors (`MoCap`; `MuJoCo`)
- [SIGGRAPH 2018](https://doi.org/10.1145/3197517.3201311), **DeepMimic**: DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills, [website](https://xbpeng.github.io/projects/DeepMimic/index.html) / [code](https://github.com/xbpeng/DeepMimic) (`MoCap`; `Bullet`)
- [SIGGRAPH Asia 2018](https://arxiv.org/abs/1810.03599), **SFV**: SFV: Reinforcement Learning of Physical Skills from Videos, [website](https://xbpeng.github.io/projects/SFV/index.html) / [code](https://github.com/akanazawa/motion_reconstruction) (`Video`; `Bullet`)
- [ICLR 2019](https://openreview.net/forum?id=BJfYvo09Y7), **HVC**: Hierarchical Visuomotor Control of Humanoids (`Unspecified`; `Unspecified`)
- [ICLR 2019](https://openreview.net/forum?id=BJl6TjRcY7), **NPMP**: Neural Probabilistic Motor Primitives for Humanoid Control (`MoCap`; `MuJoCo`)
- [SIGGRAPH Asia 2019](https://doi.org/10.1145/3355089.3356536), **DReCon**: DReCon: Data-Driven Responsive Control of Physics-Based Characters (`MoCap`; `Bullet`)
- [arXiv 2019](https://arxiv.org/abs/1812.05905), **SAC**: Soft Actor-Critic Algorithms and Applications (`Unspecified`; `MuJoCo, Minitaur`)
- [arXiv 2019](https://arxiv.org/abs/1905.11108), **SQIL**: SQIL: Imitation Learning via Reinforcement Learning with Sparse Rewards (`Unspecified`; `MuJoCo`)
- [ICML 2020](https://proceedings.mlr.press/v119/hasenclever20a.html), **CoMic**: CoMic: Complementary Task Learning & Mimicry for Reusable Skills (`MoCap`; `dm_control`)
- [CVPR 2021](https://arxiv.org/abs/2104.00683), **SimPoE**: SimPoE: Simulated Character Control for 3D Human Pose Estimation, [website](https://ye-yuan.com/simpoe/) (`Video`; `MuJoCo`)
- [SIGGRAPH 2021](https://arxiv.org/abs/2104.02180), **AMP**: AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control, [website](https://xbpeng.github.io/projects/AMP/index.html) / [code](https://github.com/xbpeng/DeepMimic) (`MoCap`; `Bullet`)
- [NeurIPS 2022](https://arxiv.org/abs/2208.07363), **MoCapAct**: MoCapAct: A Multi-Task Dataset for Simulated Humanoid Control, [website](https://microsoft.github.io/MoCapAct/) / [code](https://github.com/microsoft/MoCapAct) (`MoCap`; `dm_control`)
- [ICCV 2023](https://doi.org/10.1109/ICCV51070.2023.01000), **PHC**: Perpetual Humanoid Control for Real-Time Simulated Avatars, [website](https://github.com/ZhengyiLuo/PHC) / [code](https://github.com/ZhengyiLuo/PHC) (`MoCap`; `Isaac Gym`)
- [SIGGRAPH Asia 2023](https://doi.org/10.1145/3618375), **AdaptNet**: AdaptNet: Policy Adaptation for Physics-Based Character Control, [website](https://motion-lab.github.io/AdaptNet/) / [code](https://github.com/xupei0610/AdaptNet) (`MoCap`; `Isaac Gym`)
- [CoRL 2024](https://arxiv.org/abs/2410.01968), **Bi-Level**: Bi-Level Motion Imitation for Humanoid Robots, [website](https://sites.google.com/view/bmi-corl2024) / [code](https://github.com/wenshuaizhao/bmi) (`MoCap`; `MIT Humanoid, Isaac Gym`)
- [NeurIPS 2024](http://papers.nips.cc/paper_files/paper/2024/hash/90afd20dc776bc8849c31d61a0763a0b-Abstract-Conference.html), **Next Token**: Humanoid Locomotion as Next Token Prediction (`Unspecified`; `Unspecified`)
- [RSS 2024](https://arxiv.org/abs/2402.16796), **ExBody**: Expressive Whole-Body Control for Humanoid Robots, [website](https://expressive-humanoid.github.io/) / [code](https://github.com/chengxuxin/expressive-humanoid) (`MoCap`; `Unitree H1, Isaac Gym`)
- [SIGGRAPH Asia 2024](https://dl.acm.org/doi/full/10.1145/3680528.3687683), **PDP**: PDP: Physics-Based Character Animation via Diffusion Policy, [website](https://tml.stanford.edu/PDP.github.io/) / [code](https://github.com/Stanford-TML/PDP) (`MoCap`; `MuJoCo`)
- [CoRL 2025](https://arxiv.org/abs/2505.02833), **TWIST**: TWIST: Teleoperated Whole-Body Imitation System, [website](https://yanjieze.com/projects/TWIST/) / [code](https://github.com/YanjieZe/TWIST) (`MoCap`; `Unitree G1`)
- [RSS 2025](https://arxiv.org/abs/2502.08378), **HoST**: Learning Humanoid Standing-up Control across Diverse Postures, [website](https://taohuang13.github.io/humanoid-standingup.github.io/) / [code](https://github.com/InternRobotics/HoST) (`Unspecified`; `Unitree G1`)
- [SIGGRAPH 2025](https://arxiv.org/abs/2503.11801), **Diffuse-CLoC**: Diffuse-CLoC: Guided Diffusion for Physics-Based Character Look-Ahead Control (`MoCap`; `Isaac Gym`)
- [arXiv 2025](https://arxiv.org/abs/2503.00923), **HWC-Loco**: HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion (`MoCap`; `Unitree H1, Unitree G1, Isaac Gym`)
- [arXiv 2025](https://arxiv.org/abs/2503.10626), **NIL**: NIL: No-data Imitation Learning by Leveraging Pre-trained Video Diffusion Models (`Video`; `Unitree H1, Unitree G1, Talos, Unitree A1`)
- [arXiv 2025](https://arxiv.org/abs/2502.14814), **VB-Com**: VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception (`Unspecified`; `Unitree G1, Unitree H1`)
- [AAAI 2026](https://arxiv.org/abs/2509.13833), **Any2Track**: Track Any Motions under Any Disturbances, [website](https://zzk273.github.io/Any2Track/) / [code](https://github.com/GalaxyGeneralRobotics/OpenTrack) (`MoCap`; `Unitree G1`)
- [CVPR 2026](https://arxiv.org/abs/2512.13093), **PvP**: PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations (`MoCap`; `LimX Oli`)
- [ICRA 2026](https://arxiv.org/abs/2510.14454), **AdaMimic**: AdaMimic: Towards Adaptable Humanoid Control via Adaptive Motion Tracking, [website](https://taohuang13.github.io/adamimic.github.io/) (`Video`; `Unitree G1`)
- [ICRA 2026](https://arxiv.org/abs/2505.24266), **SignBot**: SignBot: Learning Human-to-Humanoid Sign Language Interaction, [website](https://qiaoguanren.github.io/SignBot-demo/) / [code](https://github.com/qiaoguanren/Signbot) (`Unspecified`; `Unitree H1, W1, Isaac Gym`)
- [arXiv 2026](https://arxiv.org/abs/2512.23650), **RoboPerform**: Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control (`MoCap`; `Unitree G1, Isaac Gym, MuJoCo`)
- [arXiv 2026](https://arxiv.org/abs/2511.07820), **SONIC**: SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control, [website](https://nvlabs.github.io/GEAR-SONIC/) / [code](https://github.com/NVlabs/GR00T-WholeBodyControl) (`MoCap, Video, Teleoperation`; `Unitree G1, Isaac Lab, MuJoCo`)
- [arXiv 2026](https://arxiv.org/abs/2506.01141), **Standing Tall**: Standing Tall: Sim to Real Fall Classification and Lead Time Prediction for Bipedal Robots (`Unspecified`; `Digit`)

### Skill Acquisition

Task-oriented humanoid skills such as sports, acrobatics, and long-horizon behavior.

#### Sports Skills

- [arXiv 2021](https://arxiv.org/abs/2105.12196), **Humanoid Football**: From Motor Control to Team Play in Simulated Humanoid Football (`MoCap`; `MuJoCo`)
- [ICRA 2022](https://ieeexplore.ieee.org/document/9811649), **DanceHAT**: DanceHAT: Generate Stable Dances for Humanoid Robots with Adversarial Training (`MoCap`; `NAO`)
- [SIGGRAPH 2022](https://doi.org/10.1145/3528233.3530735), **Learning Soccer Juggling**: Learning Soccer Juggling Skills with Layer-wise Mixture-of-Experts, [code](https://github.com/ZhaomingXie/soccer_juggle_release) (`MoCap`; `Physics-based simulation`)
- [SIGGRAPH 2023](https://doi.org/10.1145/3592408), **Tennis Skills**: Learning Physically Simulated Tennis Skills from Broadcast Videos, [website](https://research.nvidia.com/labs/toronto-ai/vid2player3d/) / [code](https://github.com/nv-tlabs/vid2player3d) (`MoCap, Video`; `Isaac Gym`)
- [SIGGRAPH 2024](https://doi.org/10.1145/3641519.3657437), **Table Tennis Skill**: Strategy and Skill Learning for Physics-based Table Tennis Animation, [website](https://jiashunwang.github.io/) (`MoCap`; `Isaac Gym`)
- [SIGGRAPH 2025](https://arxiv.org/abs/2505.04002), **PARC**: PARC: Physics-Based Augmentation with Reinforcement Learning for Character Controllers, [website](https://michaelx.io/parc/) / [code](https://github.com/mshoe/PARC) (`Learned Motion Priors`; `Isaac Gym`)
- [SIGGRAPH Asia 2025](https://doi.org/10.1145/3763367), **Learning to Ball**: Learning to Ball: Composing Policies for Long-Horizon Basketball Moves, [website](https://pei-xu.github.io/basketball) / [code](https://github.com/xupei0610/basketball) (`MoCap, Video`; `Isaac Gym`)
- [arXiv 2025](https://doi.org/10.48550/arXiv.2508.21043), **HITTER**: HITTER: A HumanoId Table TEnnis Robot via Hierarchical Planning and Learning, [website](https://humanoid-table-tennis.github.io) (`MoCap`; `Unitree G1, Isaac Lab`)
- [ICRA 2026](https://arxiv.org/abs/2505.12679), **Dribble Master**: Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion (`Unspecified`; `Booster T1`)
- ICRA 2026, **MAKP**: MAKP: Multi-Mode Accurate Kicking Policy for Humanoid Robots (`MoCap`; `Booster T1, Isaac Gym, MuJoCo`)
- [arXiv 2026](https://arxiv.org/abs/2510.18002), **Humanoid Goalkeeper**: Humanoid Goalkeeper: Learning from Position Conditioned Task-Motion Constraints (`Video`; `Unitree G1, Isaac Gym`)

#### Acrobatic Skills

- [NIPS 2020](https://proceedings.neurips.cc/paper/2020/hash/f76a89f0cb91bc419542ce9fa43902dc-Abstract.html), **RFC**: Residual Force Control for Agile Human Behavior Imitation and Extended Motion Synthesis, [website](https://ye-yuan.com/rfc/) / [code](https://github.com/Khrylx/RFC) (`MoCap`; `MuJoCo`)
- CoRL 2023, **Robot Parkour**: Robot Parkour Learning (`Unspecified`; `Unspecified`)
- [CoRL 2024](https://proceedings.mlr.press/v270/zhuang25a.html), **Humanoid Parkour**: Humanoid Parkour Learning, [website](https://humanoid4parkour.github.io) (`Unspecified`; `Unitree H1, Isaac Gym`)
- ICRA 2024, **Extreme Parkour**: Extreme Parkour with Legged Robots (`Unspecified`; `Unspecified`)
- [NIPS 2025](https://arxiv.org/abs/2506.12851), **KungfuBot**: KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills, [website](https://kungfu-bot.github.io/) / [code](https://github.com/TeleHuman/PBHC) (`MoCap, Video`; `Unitree G1`)
- [arXiv 2025](https://arxiv.org/abs/2502.10363), **BeamDojo**: BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds, [website](https://why618188.github.io/beamdojo) (`Unspecified`; `Unitree G1, Isaac Gym`)
- [arXiv 2025](https://doi.org/10.48550/arXiv.2509.16638), **KungfuBot2**: KungfuBot2: Learning Versatile Motion Skills for Humanoid Whole-Body Control (`Unspecified`; `Unspecified`)

#### Long-Horizon Skills

- [CoRL 2024](https://proceedings.mlr.press/v270/zhang25a.html), **WoCoCo**: WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts (`Unspecified`; `Unspecified`)
- [ICLR 2024](https://openreview.net/forum?id=OrOd8PxOO2), **PULSE**: Universal Humanoid Motion Representations for Physics-Based Control (`Unspecified`; `Unspecified`)
- [ICRA 2024](https://doi.org/10.1109/ICRA57147.2024.10610977), **Box Loco-Manipulation**: Sim-to-Real Learning for Humanoid Box Loco-Manipulation (`Unspecified`; `Unspecified`)
- CoRL 2025, **CLONE**: CLONE: Closed-Loop Whole-Body Humanoid Teleoperation for Long-Horizon Tasks, [website](https://humanoid-clone.github.io/) (`Teleoperation, MoCap`; `Unitree G1`)
- [arXiv 2025](https://arxiv.org/abs/2509.20717), **RobotDancing**: RobotDancing: Residual-Action Reinforcement Learning Enables Robust Long-Horizon Humanoid Motion Tracking (`MoCap`; `Unitree G1, Unitree H1/H1-2, Isaac Gym, MuJoCo`)
- [ICLR 2026](https://arxiv.org/abs/2512.14696), **CRISP**: CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives, [website](https://crisp-real2sim.github.io/CRISP-Real2Sim/) / [code](https://github.com/Z1hanW/CRISP-Real2Sim) (`Video`; `Isaac Gym`)
- [arXiv 2026](https://arxiv.org/abs/2602.06341), **HiWET**: HiWET: Hierarchical World-Frame End-Effector Tracking for Long-Horizon Humanoid Loco-Manipulation (`Unspecified`; `Unitree G1, Isaac Lab, MuJoCo`)
- [arXiv 2026](https://arxiv.org/abs/2602.21723), **LessMimic**: LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations, [website](https://lessmimic.github.io) (`Unspecified`; `Unspecified`)
- [arXiv 2026](https://doi.org/10.48550/arXiv.2604.14834), **Switch**: Switch: Learning Agile Skills Switching for Humanoid Robots (`Unspecified`; `Unspecified`)

### Interaction Learning

Object, scene, and human interaction behaviors.

#### Humanoid-Object Interaction

- [TOG 2020](https://doi.org/10.1145/3386569.3392474), **Catch & Carry**: Catch & Carry: Reusable Neural Controllers for Vision-Guided Whole-Body Tasks (`MoCap`; `Unspecified`)
- [arXiv 2023](https://doi.org/10.48550/arXiv.2312.04393), **PhysHOI**: PhysHOI: Physics-Based Imitation of Dynamic Human-Object Interaction, [website](https://wyhuai.github.io/physhoi-page/) (`MoCap`; `Unspecified`)
- [CoRL 2024](https://proceedings.mlr.press/v270/li25a.html), **OKAMI**: OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation, [website](https://ut-austin-rpl.github.io/OKAMI/) (`Video`; `Fourier GR1`)
- [CoRL 2024](https://arxiv.org/abs/2406.08858), **OmniH2O**: OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning, [website](https://omni.human2humanoid.com/) / [code](https://github.com/LeCAR-Lab/human2humanoid) (`MoCap, Teleoperation`; `Unitree H1`)
- [CoRL 2024](https://proceedings.mlr.press/v270/cheng25b.html), **Open-TeleVision**: Open-TeleVision: Teleoperation with Immersive Active Visual Feedback (`Teleoperation`; `Unitree H1, Fourier GR-1`)
- [CVPR 2025](https://arxiv.org/abs/2502.20390), **InterMimic**: InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions, [website](https://sirui-xu.github.io/InterMimic/) / [code](https://github.com/Sirui-Xu/InterMimic) (`MoCap`; `Isaac Gym`)
- [ICRA 2025](https://doi.org/10.1109/ICRA55743.2025.11127809), **DexMimicGen**: DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning (`Unspecified`; `Unspecified`)
- [ICRA 2025](https://doi.org/10.1109/ICRA55743.2025.11128549), **HOVER**: HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots (`Unspecified`; `Unspecified`)
- [IROS 2025](https://doi.org/10.1109/IROS60139.2025.11246340), **iDP3**: Generalizable Humanoid Manipulation with 3D Diffusion Policies, [website](https://humanoid-manipulation.github.io) (`Teleoperation`; `Fourier GR1`)
- [RA-L 2025](https://arxiv.org/abs/2409.20514), **Opt2Skill**: Opt2Skill: Imitating Dynamically-feasible Whole-Body Trajectories for Versatile Humanoid Loco-Manipulation, [website](https://opt2skill.github.io) (`Unspecified`; `Digit`)
- [RSS 2025](https://arxiv.org/abs/2505.03738), **AMO**: AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control, [website](https://amo-humanoid.github.io/) / [code](https://github.com/OpenTeleVision/AMO) (`MoCap`; `Unitree G1`)
- [arXiv 2025](https://doi.org/10.48550/arXiv.2503.13441), **HPHP**: Humanoid Policy ~ Human Policy, [website](https://human-as-robot.github.io/) (`Teleoperation`; `Unitree H1, Unitree H1-2`)
- [arXiv 2025](https://doi.org/10.48550/arXiv.2510.08807), **Humanoid Everyday**: Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation (`Teleoperation`; `Unitree humanoid`)
- arXiv 2025, **SimGenHOI**: SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and Reinforcement Learning (`Unspecified`; `Unspecified`)
- [ICRA 2026](https://arxiv.org/abs/2509.14353), **DreamControl**: DreamControl: Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion, [website](https://genrobo.github.io/DreamControl/) / [code](https://github.com/GenRobo/DreamControl/tree/main) (`Learned Motion Priors`; `Unitree G1`)
- ICRA 2026, **Embracing Bulky Objects**: Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning (`Learned Motion Priors`; `Unitree H1-2`)
- [ICRA 2026](https://arxiv.org/abs/2511.14756), **HMC**: HMC: Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation, [website](https://loco-hmc.github.io) (`Unspecified`; `Unitree G1`)
- [RSS 2026](https://arxiv.org/abs/2602.11758), **HAIC**: HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model, [website](https://haic-humanoid.github.io/) (`MoCap`; `Unitree G1`)
- arXiv 2026, **Pro-HOI**: Pro-HOI: Perceptive Root-guided Humanoid-Object Interaction (`Unspecified`; `Unspecified`)

#### Humanoid-Scene Interaction

- ICCV 2021, **SAMP**: Stochastic Scene-Aware Motion Prediction, [website](https://samp.is.tue.mpg.de) (`MoCap`; `Virtual human`)
- [SIGGRAPH 2023](https://arxiv.org/abs/2302.00883), **InterPhys**: Synthesizing Physical Character-Scene Interactions, [website](https://arxiv.org/abs/2302.00883) (`MoCap`; `Isaac Gym`)
- [ICLR 2024](https://arxiv.org/abs/2309.07918), **UniHSI**: Unified Human-Scene Interaction via Prompted Chain-of-Contacts, [website](https://xizaoqu.github.io/unihsi/) / [code](https://github.com/InternRobotics/UniHSI) (`MoCap`; `Isaac Gym`)
- [arXiv 2024](https://doi.org/10.48550/arXiv.2412.17730), **MimickingBench**: Mimicking-Bench: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking (`Unspecified`; `Unspecified`)
- [CVPR 2025](https://arxiv.org/abs/2503.19901), **TokenHSI**: TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization, [website](https://liangpan99.github.io/TokenHSI/) / [code](https://github.com/liangpan99/TokenHSI) (`MoCap`; `Isaac Gym`)
- [arXiv 2025](https://doi.org/10.48550/arXiv.2503.08299), **Distillation-PPO**: Distillation-PPO: A Novel Two-Stage Reinforcement Learning Framework for Humanoid Robot Perceptive Locomotion (`Unspecified`; `Unspecified`)
- [arXiv 2025](https://arxiv.org/abs/2512.01061), **DoorMan**: Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer (`Unspecified`; `Unitree G1`)
- [arXiv 2025](https://arxiv.org/abs/2511.14625), **Gallant**: Gallant: Voxel Grid-based Humanoid Locomotion and Local-navigation across 3D Constrained Terrains (`Unspecified`; `Unitree G1`)
- [arXiv 2025](https://doi.org/10.48550/arXiv.2506.13751), **LeVERB**: LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction (`Unspecified`; `Unspecified`)
- arXiv 2025, **PhysHSI**: PhysHSI: Towards a Real-World Generalizable and Natural Humanoid-Scene Interaction System (`Unspecified`; `Unspecified`)

#### Humanoid-Human Interaction

- [RAL 2024](https://arxiv.org/abs/2406.15833), **XGB**: XBG: End-to-End Imitation Learning for Autonomous Behaviour in Human-Robot Interaction and Collaboration, [website](https://ami-iit.github.io/xbg/) / [code](https://github.com/ami-iit/paper_cardenas_2024_ral_xbg) (`Teleoperation`; `ErgoCub`)
- [arXiv 2024](https://arxiv.org/abs/2402.04768), **ECHO**: Robot Interaction Behavior Generation based on Social Motion Forecasting for Human-Robot Interaction, [website](https://evm7.github.io/ECHO) (`Unspecified`; `JVRC-1, TIAGo++`)
- ICCV 2025, **Human-X**: Towards Immersive Human-X Interaction: A Real-Time Framework for Physically Plausible Motion Synthesis (`Unspecified`; `Unspecified`)
- [arXiv 2025](https://doi.org/10.48550/arXiv.2510.10206), **It Takes Two**: It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots (`Unspecified`; `Unspecified`)
- [arXiv 2025](https://arxiv.org/abs/2502.13134), **RHINO**: RHINO: Learning Real-Time Humanoid-Human-Object Interaction from Human Demonstrations, [website](https://humanoid-interaction.github.io) (`Unspecified`; `Unitree H1`)
- [CVPR 2026](https://arxiv.org/pdf/2601.09518), **Beyond Mimicry**: Beyond Mimicry: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations (`MoCap`; `Unitree G1`)
- arXiv 2026, **D-STAR**: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations (`Unspecified`; `Unspecified`)
- arXiv 2026, **SynAgent**: SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy (`Unspecified`; `Unspecified`)

### Generalist Humanoid Policies

Broad-coverage policies, multi-skill controllers, and foundation/VLA-style humanoid policies.

#### Skill-Guided Policies

- [SIGGRAPH Asia 2022](https://doi.org/10.1145/3550454.3555434), **ControlVAE**: ControlVAE: Model-Based Learning of Generative Controllers for Physics-Based Characters, [website](https://heyuanyao-pku.github.io/Control-VAE/) / [code](https://github.com/heyuanYao-pku/Control-VAE) (`MoCap`; `ODE`)
- [CVPR 2025](https://arxiv.org/abs/2408.15270), **SkillMimic**: SkillMimic: Learning Basketball Interaction Skills from Demonstrations, [website](https://ingrid789.github.io/SkillMimic/) / [code](https://github.com/wyhuai/SkillMimic) (`MoCap, Video`; `Isaac Gym`)
- [SIGGRAPH 2025](https://doi.org/10.1145/3721238.3730640), **SkillMimic-V2**: SkillMimic-V2: Learning Robust and Generalizable Interaction Skills from Sparse and Noisy Demonstrations (`Unspecified`; `Unspecified`)
- [arXiv 2025](https://arxiv.org/abs/2505.10918), **R2S2**: Unleashing Humanoid Reaching Potential via Real-world-Ready Skill Space (`Unspecified`; `Unspecified`)
- arXiv 2025, **SkillBlender**: SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending (`Unspecified`; `Unspecified`)
- [Actuators 2026](https://www.mdpi.com/2076-0825/15/4/212), **HAML**: HAML: Humanoid Adversarial Multi-Skill Learning via a Single Policy (`Unspecified`; `Unspecified`)
- [ICLR 2026](https://arxiv.org/abs/2412.13196), **ExBody2**: ExBody2: Advanced Expressive Humanoid Whole-Body Control, [website](https://exbody2.github.io/) (`MoCap`; `Unitree G1`)
- RA-L 2026, **CodeAct**: CodeAct: Codebook-Guided Multi-Skill Integration for Dynamic Humanoid Whole-Body Control (`Unspecified`; `Unspecified`)
- arXiv 2026, **HumanX**: HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos (`Unspecified`; `Unspecified`)
- [arXiv 2026](https://doi.org/10.48550/arXiv.2605.24592), **MuGen**: MuGen: Multi-Skill Generative Locomotion Controller for Humanoid Robots (`Unspecified`; `Unspecified`)

#### Task-Guided Policies

- [SIGGRAPH 2022](https://arxiv.org/abs/2205.01906), **ASE**: ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters, [website](https://research.nvidia.com/labs/toronto-ai/ASE/) / [code](https://github.com/nv-tlabs/ASE) (`MoCap`; `Isaac Gym`)
- [SIGGRAPH 2023](https://arxiv.org/abs/2305.02195), **CALM**: CALM: Conditional Adversarial Latent Models for Directable Virtual Characters, [website](https://xbpeng.github.io/projects/CALM/index.html) / [code](https://github.com/NVlabs/CALM/) (`MoCap`; `Isaac Gym`)
- [arXiv 2023](https://doi.org/10.48550/arXiv.2309.11351), **C-ASE**: C-ASE: Learning Conditional Adversarial Skill Embeddings for Physics-based Characters (`Unspecified`; `Unspecified`)
- [ECCV 2024](https://arxiv.org/abs/2502.05641), **MHC**: Generating Physically Realistic and Directable Human Motions from Multi-Modal Inputs, [website](https://idigitopia.github.io/projects/mhc/) / [code](https://github.com/osudrl/masked-humanoid-controller) (`MoCap`; `Isaac Gym`)
- [SIGGRAPH Asia 2024](https://doi.org/10.1145/3687951), **MaskedMimic**: MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting, [code](https://github.com/DanielTruong99/MaskedMimic) (`MoCap`; `Isaac Gym`)
- [arXiv 2024](https://doi.org/10.48550/arXiv.2412.04368), **FB-AW**: Finer Behavioral Foundation Models via Auto-Regressive Features and Advantage Weighting (`Unspecified`; `Unspecified`)
- [ICLR 2025](https://openreview.net/forum?id=9sOR0nYLtz), **MOTIVO**: Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models (`Unspecified`; `Unspecified`)
- [arXiv 2025](https://doi.org/10.48550/arXiv.2509.13780), **BFM-for-HR**: Behavior Foundation Model for Humanoid Robots (`Unspecified`; `Unspecified`)
- arXiv 2025, **BFM-Zero**: BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning (`Unspecified`; `Unspecified`)

#### Vision-Language-Guided Policies

- [NIPS 2023](https://arxiv.org/abs/2312.17135), **InsActor**: InsActor: Instruction-Driven Physics-Based Characters, [website](https://jiawei-ren.github.io/projects/insactor/index.html) / [code](https://github.com/MotrixLab/insactor) (`MoCap`; `Brax`)
- [CoRL 2024](https://arxiv.org/abs/2406.10454), **HumanPlus**: HumanPlus: Humanoid Shadowing and Imitation from Humans, [website](https://humanoid-ai.github.io/) / [code](https://github.com/MarkFzp/humanplus) (`MoCap, Teleoperation`; `Unitree H1`)
- [NIPS 2024](https://arxiv.org/abs/2502.14795), **HumanVLA**: Humanoid-VLA: Towards Universal Humanoid Control with Visual Integration (`MoCap`; `Isaac Gym`)
- [ICLR 2025](https://arxiv.org/abs/2410.03441), **CLoSD**: CLoSD: Closing the Loop between Simulation and Diffusion for Multi-Task Character Control, [website](https://guytevet.github.io/CLoSD-page/) / [code](https://github.com/GuyTevet/CLoSD) (`Learned Motion Priors`; `Isaac Gym`)
- RSS 2025, **LangWBC**: LangWBC: Language-directed Humanoid Whole-Body Control via End-to-end Learning (`Unspecified`; `Unspecified`)
- [arXiv 2025](https://doi.org/10.48550/arXiv.2503.14734), **GR00T N1**: GR00T N1: An Open Foundation Model for Generalist Humanoid Robots (`Unspecified`; `Unspecified`)
- arXiv 2025, **Humanoid-LLA**: Humanoid-LLA: Open-Vocabulary Humanoid Whole-Body Control with Large Language Action Model (`Unspecified`; `Unspecified`)
- [arXiv 2025](https://arxiv.org/abs/2512.11047), **WholeBodyVLA**: WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control, [website](https://opendrivelab.com/WholeBodyVLA) (`Video, Teleoperation`; `AgiBot X2`)
- [CVPR 2026](https://arxiv.org/abs/2511.19236), **SENTINEL**: SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control (`MoCap`; `Unitree G1`)
- [CVPR 2026](https://arxiv.org/abs/2511.15200), **VIRAL**: VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation (`Teleoperation`; `Unitree G1`)
- [ICLR 2026](https://arxiv.org/abs/2511.00041), **BiBo**: Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World, [code](https://github.com/Shadow-Dream/BiBo) (`MoCap`; `Isaac Gym`)
- [ICRA 2026](https://arxiv.org/abs/2510.03022), **HumanoidExo**: HumanoidExo: Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton, [website](https://humanoid-exo.github.io/) (`Teleoperation`; `Unitree G1`)
- arXiv 2026, **Psi0**: Psi0: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation (`Unspecified`; `Unspecified`)

## Data Format

The canonical data file is [`data/papers.json`](data/papers.json). Each entry keeps the full paper title, method name, venue, year, data source, method category, method subcategory, platform, and links.

```json
{
  "method_name": "DeepMimic",
  "title": "DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills",
  "year": 2018,
  "venue": "SIGGRAPH",
  "data_sources": ["MoCap"],
  "primary_category": "motion-retargeting-and-tracking",
  "subcategory": "physics-based-motion-tracking",
  "platforms": ["Bullet"],
  "links": {"paper": "https://doi.org/10.1145/3197517.3201311", "code": "", "project": ""}
}
```

## Contributing

Please keep exactly one `primary_category` and one `subcategory` per paper. If a paper spans multiple ideas, put the overlap in `data_sources`, `tags`, `platforms`, `links`, and `notes`.

After editing `data/papers.json`, regenerate and validate the list:

```bash
python scripts/generate_readme.py
python scripts/validate_papers.py
```

## Citation

If you use this list, please cite the survey paper. A formal BibTeX entry can be added once the final publication metadata is available.
