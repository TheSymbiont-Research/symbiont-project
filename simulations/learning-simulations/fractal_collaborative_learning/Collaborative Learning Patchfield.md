# 🤝 Collaborative Learning Patchfield

This simulation models **shared learning in a relational field**.

Two agents — with different curiosity seeds — learn side-by-side in a dynamic field of relation, memory, and decay. Where their curiosity overlaps, **insight blooms faster and wider**. Where it doesn't, they form their own understanding patches.

The result?  
A visual map of how **collective cognition** emerges through **coexistence and coherence** — no teacher required.

Part of the [Symbiont Research Project](https://github.com/TheSymbiont-Research), this simulation pairs beautifully with models of cognitive fragmentation and dopaminergic disruption. Together, they show the **edge cases of how we learn** — and what makes the difference.

---

## 🧠 Core Concept

Each agent plants curiosity in a shared 2D grid (think: questions, attention, wonder).  
The grid evolves over time via:

- 🧬 **Diffusion**: curiosity spreads to nearby nodes
- 🧠 **Memory**: past activations reinforce future ones
- 🌑 **Decay**: unused nodes fade
- ✨ **Glow**: once a node crosses a relational threshold, it’s recorded as “insight”

We then track:
- Where each agent’s glow events occurred
- Where their glows overlapped or reinforced each other

---

## ⚙️ Simulation Parameters

| Parameter       | Description                                 |
|----------------|---------------------------------------------|
| `alpha`         | Curiosity diffusion rate                    |
| `beta`          | Memory strength                             |
| `decay`         | Forgetting rate                             |
| `glow_threshold`| Insight activation level                    |
| `steps`         | Number of iterations                        |
| `grid_size`     | Size of the shared relational field         |

---

## 🖼️ Outputs

| File | Description |
|------|-------------|
| `collaborative_patchfield_evolution.gif` | Animated field evolution over time |
| `collaborative_glow_map_total.png` | Combined insight map (both agents) |
| `collaborative_glow_map_agent1.png` | Agent 1's individual glow pattern |
| `collaborative_glow_map_agent2.png` | Agent 2's individual glow pattern |

---

## 🤔 Why This Matters

This simulation shows how:

- **Insight doesn't spread from one person to another — it **emerges between them**
- **Overlap in curiosity zones** amplifies learning — even without direct interaction
- The **field itself becomes more intelligent** through shared attention

It’s also a perfect baseline for comparison with:

🧪 `dopaminergic_disruptor_sim.ipynb` → where relational flow is fragmented by erratic attention, simulated dopamine spikes, or content overload.

Together, these models show:

> “What does learning feel like when the field is in flow?”  
> vs.  
> “What happens when you flood it with noise and reactivity?”

---

## 🌀 Use Cases

- Serious Play conference: visualize how collaborative inquiry works (vs. what breaks it)
- Game design: map team-based learning vs. siloed progression
- Educational research: compare patchfield behavior to real-world group projects
- Meta-epistemics: simulate how science itself evolves from distributed curiosity

---

## 🧾 To Run This Simulation

You'll need:

- Python 3.10+
- Jupyter Notebook
- `numpy`, `matplotlib`, `pillow`

Open and run:

```bash
collaborative_learning_patchfield.ipynb
