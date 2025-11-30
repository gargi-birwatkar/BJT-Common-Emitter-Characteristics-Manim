# 🚀 BJT Animated: An Electronics Learning Series

![Python](https://img.shields.io/badge/python-3.11-blue)
![Manim](https://img.shields.io/badge/manim-Community-orange)

Welcome to the repository for a complete series of **Manim animations** dedicated to the **Bipolar Junction Transistor (BJT)**!  

This project aims to demystify one of the most fundamental components in electronics by providing **clear, step-by-step visual explanations** of its structure, characteristics, and application in amplifier circuits.

---

## 🎯 Learning Goals

By exploring these animations, students will:

- Understand the **structure of NPN and PNP BJTs**.
- Visualize **electron and hole flow** in **Active, Cutoff, and Saturation regions**.
- Learn how to **plot and interpret input/output characteristics**.
- Analyze **CE amplifier circuits** using **DC load lines and Q-points**.

---

## 🎬 Three-Part BJT Video Series

The series is broken down into three logical parts, taking you from transistor physics to practical amplifier applications.

---

### 1. The Transistor Uncovered: Structure and Basic Working

Your introduction to BJTs! Visualize **NPN vs PNP devices** and understand the critical roles of the **Emitter, Base, and Collector**. Learn how a small base current controls a large collector current.  

![BJT Structure Preview](media/bjt_structure_preview.gif)

| Concept | What You'll See |
| :--- | :--- |
| **Structure** | Detailed doping levels of the three regions. |
| **Working Principle** | Animation of current flow in the **Active Region**. |


---

### 2. Common Emitter (CE) Characteristics Explained

Explore the **Common Emitter configuration**, the foundation of transistor amplifiers. Dynamic plots show **input and output characteristics** clearly, with visualized operating regions.

![CE Characteristics Preview](media/ce_characteristics_preview.gif)

| Characteristic | Key Insight |
| :--- | :--- |
| **Input Curve** | How $V_{BE}$ controls $I_B$ (like a diode). |
| **Output Curve** | How $I_C$ changes with $V_{CE}$ for different $I_B$ values. |
| **Operating Regions** | Visual animation of **Cutoff**, **Active**, and **Saturation** regions. |

---

### 3. Amplifier Analysis: Load Line and Q-Point

Bridge theory with practice! Analyze a **CE amplifier circuit** using the **DC Load Line** on the output characteristics to determine the optimal **Q-Point** for distortion-free amplification.

![Load Line Preview](media/load_line_preview.gif)

| Analysis Tool | Formula and Purpose |
| :--- | :--- |
| **DC Load Line** | $V_{CE} = V_{CC} - I_C R_C$ (Defines the circuit limits) |
| **Q-Point** | Optimal operating point for the transistor. |

---

## 🛠️ Source Code & Tools

This repository contains all the **Manim Python scripts** used to generate these animations:

- `bjt_fundamentals.py`  
- `ce_characteristics.py`  
- `ce_amplifier_analysis.py`  

**Static Charts:** High-quality PNGs of characteristic curves are included in the `media/` folder for quick reference.

---

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/BJT-Animated.git
cd BJT-Animated

# Install dependencies
pip install manim numpy

# Render the first animation
manim -pql bjt_fundamentals.py npntransistor
````

* Flags: `-p` → preview after rendering, `-ql` → quick low-quality render (use `-qm` or `-qh` for higher quality)

---

## 🤝 Contributing

We welcome contributions! You can:

* Add animations for other transistor configurations.
* Improve existing animations with better visuals or labeling.
* Suggest corrections or enhancements to this README.

