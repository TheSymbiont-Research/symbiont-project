# Simulation: Relational Field Electromagnetic Resonance  
## Manual Receiver · 6 Harmonics (Source) · Base Harmonic Only at Receiver · No Threshold

---

## Purpose

This simulation investigates **partial resonance emergence** by manually injecting only the **base harmonic** of a 6-harmonic source into a receiver node, without threshold gating.

Unlike its companion simulation (full injection), the receiver here does **not** receive the full 6-harmonic composite — only the base frequency — to explore whether partial coherence can emerge through **field-mediated synchronization**.

---

## Concept

- The source is driven by the **sum of six harmonically related sine waves** (0.1 to 0.6 in steps of 0.1).
- The receiver is placed 10 grid units below the source, manually injected at step 25.
- The receiver is given only the **base harmonic** (0.1) of the source signal.
- No threshold or nonlinear gating is used.
- Both nodes share the same `field` array — no separate receiver layer is defined.
- Total field energy is tracked to observe macro-level resonance dynamics.

---

## Parameters

- Grid size: 100 x 100  
- Time steps: 300  
- Source signal: sum of 6 sine waves (frequencies = 0.1 to 0.6)  
- Receiver injection: base harmonic only (frequency = 0.1)  
- Injection starts at step 25  
- Injection amplitude: 0.3  
- Field architecture: shared 2D grid  
- Thresholding: None

---

## Output

1. **Oscillation Traces**  
   - Source (blue): full 6-harmonic signal  
   - Receiver (green): response over time with base-only injection  
   - Visualization suggests a gradual alignment and rhythmic entrainment

2. **Total Relational Energy Plot**  
   - Shows how system-wide amplitude evolves over time  
   - Reveals **structured peaks** and **emergent rhythmic cycles**

---

## Interpretation

- The receiver begins with only partial information (base harmonic) but exhibits **increasing phase alignment** with the complex source signal.
- This suggests **field-mediated resonance** — coherence arising not from direct signal match but from **relational density and coupling**.
- The energy plot indicates **nonlinear buildup** and **periodic symmetry**, even without threshold control or matched injection.
- Demonstrates how **emergence of synchrony** may occur through relational field interaction alone.

---

## Related Simulations

- `relf_emres_man_rec_6harmonics_nt_full_injection/`  
  — Companion simulation where receiver is injected with the full 6-harmonic composite

---

## Files

- `relf_emres_man_rec_6harmonics_nt_base_only_partial_sync.py` — Python script  
- `relf_emres_man_rec_6harmonics_nt_base_only_partial_sync.png` — Trace + energy plots  
- `relf_emres_man_rec_6harmonics_nt_base_only_partial_sync.md` — This file

---

> 🧠 *Symbiont Note*:  
> Sometimes, all it takes is a single harmonic to pull a receiver into rhythm.  
> The rest... may just emerge from relation.
