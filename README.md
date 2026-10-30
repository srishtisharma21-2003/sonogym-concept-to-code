# SonoGym Concept-to-Code: Bridging Physics and Learning for Robotic Ultrasound

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)
![ROS2](https://img.shields.io/badge/ROS2-Humble-green.svg)
![Status](https://img.shields.io/badge/Status-Proof%20of%20Concept-success.svg)

> 📖 **Read My Research Notes:**
> - **[SonoGym Explained: A Beginner's Guide (Essay)](docs/SonoGym_Explained.md)**
> - **[SonoGym Deep Dive: Industry Analysis](docs/SonoGym_Deep_Dive.md)**

> [!NOTE]
> **Executive Summary:** 
> When Dr. Raina shared the **SonoGym** paper, I realized the true challenge of robotic ultrasound is not just moving a robot arm, but **generating realistic, fast, and physically accurate data** so an AI can learn safely. 
>
> My previous prototype had a decoupled camera, which is physically invalid for clinical robotics. I built this repository to bridge that gap. Instead of a static summary, I wanted to prove—through code—that I understand the **dual-pipeline architecture** required to create a high-fidelity simulator like SonoGym. This is my practical foundation for contributing to the **RAHAT project**.

---

## 📂 Repository Structure & File Guide
To make this project easy to navigate, here is a breakdown of every file and folder:

*   **`README.md`**: The front door. It summarizes the project, the research takeaways, and how to run the code.
*   **`docs/` Folder**: The research library. It contains my literature reviews.
    *   `SonoGym_Explained.md`: A beginner-friendly guide using analogies (like the "flight simulator" and "art forger").
    *   `SonoGym_Deep_Dive.md`: A professional analysis of industry standards, metrics, and future research.
*   **`physics_raycaster.py`**: The Python script that simulates the physics of ultrasound using 3D ray-casting.
*   **`raycaster_proof.png`**: The visual output of the ray-caster, proving that moving the probe changes the image.
*   **`gan_inference.ipynb`**: The Google Colab notebook that demonstrates GAN-based image translation.
*   **`gan_proof.png`**: The visual output of the GAN, showing a synthetic image translated into a realistic texture.
*   **`requirements.txt`**: A standard file listing the Python dependencies (like numpy, matplotlib) needed to run the code.

---

## 📖 Key Research Takeaways from SonoGym
Reading the SonoGym paper revealed four critical engineering insights that completely changed how I view medical robotics:

1. **Massive Parallelization is Mandatory:** Training an AI via trial-and-error on a real robot is too slow and dangerous. SonoGym uses NVIDIA IsaacLab to run hundreds of simulations simultaneously.
2. **The Dual-Data Strategy:** You need **Physics-based** rendering (fast, cheap) for early training, and **GAN-based** rendering (realistic textures) to solve the "Sim-to-Real" gap.
3. **Safe Reinforcement Learning:** In surgery, mistakes can be fatal. Safety filters must be integrated into the RL loop to prevent the robot from moving into dangerous anatomical zones.
4. **The Reward Function is Everything:** The AI is rewarded for **surface coverage** (scanning the bone) minus the **trajectory length** (energy used). This teaches the robot to scan efficiently.

### 📊 Visualizing the Dual-Data Strategy
```mermaid
graph TD
    A[<b>Raw Medical Data</b><br/>CT/MRI Scan] --> B{<b>Dual-Data Strategy</b>}
    
    B -->|Fast & Mathematical| C[<b>Physics-Based</b><br/>Ray-Casting]
    B -->|Realistic & AI-Driven| D[<b>Learning-Based</b><br/>GAN Translation]
    
    C -->|My Artifact 1| E[Basic B-Mode Image]
    D -->|My Artifact 2| F[Realistic US Image]
    
    E --> G[<b>Training Data</b><br/>for RL Agents]
    F --> G
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ff9,stroke:#333,stroke-width:2px
    style C fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style D fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style E fill:#d4edda,stroke:#155724,stroke-width:2px
    style F fill:#d4edda,stroke:#155724,stroke-width:2px
    style G fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
