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

| File / Folder | Type | What it does & Why it's important |
| :--- | :--- | :--- |
| 📄 **`README.md`** | Documentation | The front door. Summarizes the project, research takeaways, and how to run the code. |
| 📁 **`docs/`** | Documentation | A research library containing deep-dive essays on the SonoGym architecture. |
| 🐍 **`physics_raycaster.py`** | Python Code | Simulates ultrasound physics using 3D ray-casting. Proves the probe's pose controls the image. |
| 🖼️ **`raycaster_proof.png`** | Image | Visual proof showing that moving the probe changes the ultrasound image (fixing the decoupled camera flaw). |
| ☁️ **`gan_inference.ipynb`** | Jupyter Notebook | A Google Colab notebook running a Pix2Pix AI model. Demonstrates AI domain translation (Sim-to-Real). |
| 🖼️ **`gan_proof.png`** | Image | Visual proof showing an AI translating a basic edge map into a realistic medical texture. |
| 📝 **`requirements.txt`**| Config File | Lists the Python libraries (numpy, matplotlib, etc.) required to run the code locally. |

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
```

---

## 🔬 Artifact 1: The Physics-Based Pipeline (Ray-Casting)

> [!IMPORTANT]  
> **The Problem:** My previous simulation suffered from a "decoupled camera" (the image didn't depend on the robot's pose). In reality, an ultrasound image is a direct function of the probe's kinematic state intersecting with tissue.

**The Code Logic:** 
The `physics_raycaster.py` script generates a 3D voxel phantom (simulating tissue and bone). It then casts an array of rays from a virtual probe into this phantom. If a ray hits a high-density object (bone), it records the depth and assigns a pixel intensity. 

**Why I did this:** This mirrors SonoGym's **Model-Based** pipeline. By moving the probe and watching the image change, I am physically proving that the sensor must be rigidly attached to the end-effector.

<div align="center">
  <img src="raycaster_proof.png" alt="Raycaster Proof" width="800"/>
  <p><i>Proof: As the probe translates and rotates, the US image dynamically changes, proving spatial dependency.</i></p>
</div>

### 💻 How to Run Artifact 1 (Local Setup)
```bash
# 1. Install dependencies (also listed in requirements.txt)
pip install numpy matplotlib

# 2. Run the ray-caster script
python physics_raycaster.py

# 3. View the output
# The script will generate and open 'raycaster_proof.png'
```

---

## 🧠 Artifact 2: The Learning-Based Pipeline (GAN Translation)

> [!IMPORTANT]  
> **The Problem:** Physics-based rendering is fast but lacks complex tissue textures and shadows, causing a **Sim-to-Real domain shift**. AI models trained on perfect synthetic data often fail on real patients.

**The Code Logic:** 
Because training a GAN from scratch requires massive computational power, I used a pre-trained **Pix2Pix** conditional GAN. I designed a Google Colab notebook (`gan_inference.ipynb`) that loads the model weights, takes a source domain (a synthetic edge map simulating anatomical boundaries), and translates it into a realistic target domain.

**Why I did this:** This mirrors SonoGym's **Learning-Based** pipeline. It proves I understand how researchers use domain translation to generate photorealistic ultrasound textures that can train robust AI agents.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1fiCL4CHXTXOg0WVSlJBjpmegANSpcvmE)

**Direct Link:** [Click here to view the GAN inference notebook in Google Colab](https://colab.research.google.com/drive/1fiCL4CHXTXOg0WVSlJBjpmegANSpcvmE)

<div align="center">
  <img src="gan_proof.png" alt="GAN Proof" width="600"/>
  <p><i>Proof: A Pix2Pix GAN translating a basic edge map into a complex, realistic texture.</i></p>
</div>

### 💻 How to Run Artifact 2 (Google Colab)
Because this requires PyTorch and GPU acceleration, I utilized Google Colab. 
1. Click the "Open in Colab" badge or the direct link above.
2. Ensure your runtime is set to **T4 GPU** (Runtime -> Change runtime type).
3. Run the cells sequentially to generate the GAN inference.

---

## 💡 Lessons Learned
- **Physics is hard to fake:** Writing the ray-caster taught me that generating valid ultrasound images requires a deep understanding of geometry and kinematics.
- **Sim-to-Real is the bottleneck:** Training AI on perfect data fails in reality. Using GANs to hallucinate realistic textures is the bridge.
- **The importance of documentation:** Building the code is only half the job. If another researcher cannot understand and reproduce my work, the code is useless.

---

## 🎯 My Action Plan for the RAHAT Project
Based on my studies of SonoGym, here is my proposed roadmap for integrating these concepts into the RAHAT project.

```mermaid
gantt
    title Roadmap for RAHAT Project Contribution
    dateFormat  YYYY-MM-DD
    section Phase 1: Kinematics
    ROS2 TF2 Probe Attachment :active, des1, 2026-11-01, 14d
    section Phase 2: AI Integration
    Replace CV with TinyUNet :         des2, after des1, 21d
    section Phase 3: Autonomy
    Implement PPO RL Loop    :         des3, after des2, 21d
