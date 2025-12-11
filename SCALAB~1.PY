"""
Script: scalability_stress_test_simulation.py
Purpose: Simulate stress test for system scalability under increasing load
"""

import matplotlib.pyplot as plt
import numpy as np

# Simulated load (transactions per second)
load = np.linspace(100, 5000, 50)
response_time_auto = 1000 / (100 + 0.01 * load**1.5) + np.random.normal(0, 10, 50)
response_time_manual = 5000 / (50 + 0.005 * load) + np.random.normal(0, 20, 50)

plt.figure(figsize=(10, 6))
plt.plot(load, response_time_auto, label='Automated System', marker='o')
plt.plot(load, response_time_manual, label='Traditional Method', marker='s')
plt.xlabel("Transaction Load (tps)")
plt.ylabel("Response Time (ms)")
plt.title("Scalability Stress Test Simulation")
plt.legend()
plt.grid(True)
plt.savefig("scalability_stress_test.png")