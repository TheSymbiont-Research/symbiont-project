# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 21:17:36 2025

@author: Carmen VQ
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
grid_size = 100
timesteps = 300
injection_step = 25
source_center = (grid_size // 2, grid_size // 2)
receiver_center = (grid_size // 2 + 10, grid_size // 2)
omega_base = 0.1

# Harmonic frequencies
harmonics = [1, 2, 3, 4, 5, 6]
frequencies = [omega_base * h for h in harmonics]

# Initialization
field = np.zeros((grid_size, grid_size))
receiver_trace = []
source_trace = []

# Source signal: sum of harmonics
t = np.arange(timesteps)
source_signal = sum(np.sin(w * t) for w in frequencies)

# Simulation loop
for step in range(timesteps):
    # Inject source
    field[source_center] = source_signal[step]

    # Inject manual receiver without threshold
    if step >= injection_step:
        field[receiver_center] += 0.3 * np.sin(frequencies[0] * step)

    # Capture traces
    source_trace.append(field[source_center])
    receiver_trace.append(field[receiver_center])

# Plot results
fig, axs = plt.subplots(2, 1, figsize=(10, 6), height_ratios=[2, 1])
axs[0].plot(source_trace, label='Source (sum of 6 harmonics)', color='blue')
axs[0].plot(receiver_trace, label='Manual Receiver', color='green')
axs[0].set_title('Relational Oscillation Traces – 6 Harmonic Components (Long Run)')
axs[0].set_xlabel('Time Step')
axs[0].set_ylabel('Amplitude')
axs[0].legend()

# Energy over time
total_energy = [np.abs(s) + np.abs(r) for s, r in zip(source_trace, receiver_trace)]
axs[1].plot(total_energy, color='purple')
axs[1].set_title('Total Relational Energy Over Time')
axs[1].set_xlabel('Time Step')
axs[1].set_ylabel('Total Amplitude')

plt.tight_layout()
plt.show()
