# SonoGym Concept-to-Code: Bridging Physics and Learning for Robotic Ultrasound

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)
![ROS2](https://img.shields.io/badge/ROS2-Humble-green.svg)
![Status](https://img.shields.io/badge/Status-Proof%20of%20Concept-success.svg)

> [!NOTE]
> **Executive Summary:** 
> When Dr. Raina shared the **SonoGym** paper, I realized the true challenge of robotic ultrasound is not just moving a robot arm, but **generating realistic, fast, and physically accurate data** so an AI can learn safely. 
>
> My previous prototype had a decoupled camera, which is physically invalid for clinical robotics. I built this repository to bridge that gap. Instead of a static summary, I wanted to prove—through code—that I understand the **dual-pipeline architecture** (Physics-based vs. Learning-based) required to create a high-fidelity simulator like SonoGym. This is my practical foundation for contributing to the **RAHAT project**.

---

## 📖 Key Research Takeaways from SonoGym
Reading the SonoGym paper revealed four critical engineering insights that completely changed how I view medical robotics:

1. **Massive Parallelization is Mandatory:** Training an AI via trial-and-error on a real robot is too slow and dangerous. SonoGym uses NVIDIA IsaacLab to run hundreds of simulations simultaneously.
2. **The Dual-Data Strategy:** You need **Physics-based** rendering (fast, cheap) for early training, and **GAN-based** rendering (realistic textures) to solve the "Sim-to-Real" gap.
3. **Safe Reinforcement Learning:** In surgery, mistakes can be fatal. Safety filters must be integrated into the RL loop to prevent the robot from moving into dangerous anatomical zones.
4. **The Reward Function is Everything:** The AI is rewarded for **surface coverage** (scanning the bone) minus the **trajectory length** (energy used). This teaches the robot to scan efficiently.

### 📊 Visualizing the Dual-Data Strategy
```mermaid
graph LR
    A[Raw Medical Data / CT] --> B{Which Method?}
    
    B -->|Fast & Mathematical| C(Physics-Based Ray-Casting)
    B -->|Realistic & AI-Driven| D(GAN Domain Translation)
    
    C -->|My Artifact 1| E[Generates Basic B-Mode US]
    D -->|My Artifact 2| F[Generates Realistic US Textures]
    
    E --> G[Training Data for RL Agent]
    F --> G
    
    style C fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style D fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style G fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
