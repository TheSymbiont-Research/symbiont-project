# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 21:31:12 2025

@author: Carmen VQ
"""

import numpy as np
import matplotlib.pyplot as plt

# Grid and time setup
size = 100
timesteps = 300
source_strength = 1.0

# Frequencies for two sources (4 harmonics each)
omega_A = np.array([0.1, 0.2, 0.3, 0.4])
omega_B = omega_A * 1.05  # Slightly detuned harmonics

# Initialize oscillation arrays
source_trace_A = []
source_trace_B = []
field_energy = []

# Field (not evolved spatially here, just tracking total amplitude of source interactions)
field = np.zeros((size, size))
center_A = (30, 50)
center_B = (70, 50)

for t in range(timesteps):
    time = t / 10.0  # time scaling factor

    # Source A signal
    signal_A = np.sum([np.sin(w * time) for w in omega_A])
    source_trace_A.append(signal_A)

    # Source B signal
    signal_B = np.sum([np.sin(w * time) for w in omega_B])
    source_trace_B.append(signal_B)

    # Update field manually (accumulate energy at source points)
    field[center_A] = signal_A
    field[center_B] = signal_B

    # Total field energy: sum of absolute values
    total_energy = np.sum(np.abs(field))
    field_energy.append(total_energy)

# --- Plotting ---
fig, axs = plt.subplots(2, 1, figsize=(12, 6), gridspec_kw={'height_ratios': [2, 1]})

# Oscillation traces
axs[0].plot(source_trace_A, label="Source A (4 harmonics)", color='blue')
axs[0].plot(source_trace_B, label="Source B (4 harmonics)", color='green')
axs[0].set_title("Relational Oscillation Traces – Dual Sources (4 Harmonics Each)")
axs[0].set_xlabel("Time Step")
axs[0].set_ylabel("Amplitude")
axs[0].legend()
axs[0].grid(True)

# Field energy over time
axs[1].plot(field_energy, color='purple')
axs[1].set_title("Total Relational Energy Over Time")
axs[1].set_xlabel("Time Step")
axs[1].set_ylabel("Total Amplitude")
axs[1].grid(True)

plt.tight_layout()
plt.show()
