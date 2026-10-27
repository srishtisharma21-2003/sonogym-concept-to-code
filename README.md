# sonogym-concept-to-code# SonoGym Concept-to-Code: Bridging Physics and Learning for Robotic Ultrasound

> **Context:** Following Dr. Deepak Raina's feedback regarding the "decoupled camera" limitation in my initial RAHAT prototype, I developed this repository to practically internalize the dual-pipeline architecture of **SonoGym**. Instead of a static summary, this repository provides executable proofs of concept demonstrating both the **Model-Based (Physics)** and **Learning-Based (GAN)** approaches to ultrasound synthesis. 

---

## 🏗️ System Architecture Overview

The following diagram illustrates how this repository maps to the high-level requirements of robotic ultrasound simulation (RAHAT / SonoGym), addressing the gap between raw anatomical data and realistic B-mode image generation.

```mermaid
graph TD
    A[3D Anatomical Data / CT] --> B(Dual Simulation Engine)
    
    B -->|Model-Based: Fast| C[Ray-Casting & Acoustic Impedance]
    B -->|Learning-Based: Realistic| D[Conditional GAN / Pix2Pix]
    
    C --> E(Generated B-Mode US Image)
    D --> E
    
    E --> F[Closed-Loop Control]
    F -->|TF2 Kinematics| G[Robotic Arm End-Effector]
    G -.->|Pose Updates| C
    
    classDef physics fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef gan fill:#fff3e0,stroke:#e65100,stroke-width:2px;
    classDef core fill:#f3e5f5,stroke:#4a148c,stroke-width:2px;
    
    class C physics;
    class D gan;
    class B,F core;
