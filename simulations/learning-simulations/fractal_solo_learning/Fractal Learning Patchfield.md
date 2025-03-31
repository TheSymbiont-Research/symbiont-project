# 🧠 Fractal Learning Patchfield

A simulation of how **understanding emerges** from the interplay of curiosity, memory, relation, and decay — no teacher, no goal, no central planner. Just the field doing its thing.

This model is part of the [Symbiont Project](https://github.com/TheSymbiont-Research), where we explore cognition, learning, and planetary repair using relational dynamics, open-source simulations, and questionable sci-fi humor.

---

## 📊 What This Simulation Does

This simulation visualizes how **learning happens fractally** in a relational field:

- **Curiosity sparks** are dropped into a 2D grid.
- Nodes activate, **spread** energy to their neighbors.
- **Memory kernels** reinforce frequently visited zones.
- **Unused nodes decay** (they’re forgotten).
- **Insight "glow" events** emerge when local activity passes a threshold.

At the end, you get:

- A **GIF** of the full field evolution
- A **heatmap** of where understanding bloomed

---

## 🌱 Why This Matters

This sim shows that:

- **Cognition is field-based**, not linear
- **Insight emerges**, it’s not delivered
- **Memory, curiosity, and decay** are enough to simulate learning
- The **glow of understanding** is a threshold event — not a goal, but a pattern

You didn’t program learning.
You programmed **relation** — and learning *happened*.

---

## 🔧 How It Works

```python
R[t] = R[t-1] 
     + α ⋅ diffusion(R[t-1]) 
     + β ⋅ memory(R[:t]) 
     - decay ⋅ R[t-1]
