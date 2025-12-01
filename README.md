# 🚀 BJT Animated: An Electronics Learning Series

![Python](https://img.shields.io/badge/python-3.11-blue)
![Manim](https://img.shields.io/badge/manim-Community-orange)

Welcome to the repository for a complete series of **Manim animations** dedicated to the **Bipolar Junction Transistor (BJT)**!  

This project aims to demystify one of the most fundamental components in electronics by providing **clear, step-by-step visual explanations** of its structure, characteristics, and application in amplifier circuits.

---

## 🎯 Learning Goals

By exploring these animations, students will:

- Understand the **structure of NPN  BJTs**.
- Visualize **electron and hole flow** in **Active, Cutoff, and Saturation regions**.
- Learn how to **plot and interpret input/output characteristics**.

---

## 🎬 Three-Part BJT Video Series

The series is broken down into three logical parts, taking you from transistor physics to practical amplifier applications.

---

### 1. The Transistor Uncovered: Structure and Basic Working

Your introduction to BJTs! Visualize **NPN device** and understand the critical roles of the **Emitter, Base, and Collector**. Learn how a small base current controls a large collector current.  

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

**File Name:
   output curve:- outputchara.py
   input curve:- input.py**
---

---

## 🛠️ Source Code & Tools

This repository contains all the **Manim Python scripts** used to generate these animations:

   bjt working and fundamentals:- project.py
   output curve:- outputchara.py
   input curve:- input.py

---

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/BJT-Animated.git
cd BJT-Animated

# Install dependencies
pip install manim numpy

# Render the first animation
manim -pql project.py npntransistor
````

* Flags: `-p` → preview after rendering, `-ql` → quick low-quality render (use `-qm` or `-qh` for higher quality)

---

## 🤝 Contributing

We welcome contributions! You can:

* Add animations for other transistor configurations.
* Improve existing animations with better visuals or labeling.
* Suggest corrections or enhancements to this README.

