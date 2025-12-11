"""
Script: adaptive_learning_curve_analysis.py
Purpose: Simulate learning curves of automated AML systems over time
"""

import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1, 37)
baseline_accuracy = 70
learning_curve = baseline_accuracy + 25 * (1 - np.exp(-0.08 * months)) + np.random.normal(0, 0.5, 36)

plt.figure(figsize=(10, 6))
plt.plot(months, learning_curve, label="Detection Accuracy", marker='o')
plt.axhline(y=baseline_accuracy, color='red', linestyle='--', label="Baseline Accuracy")
plt.xlabel("Training Time (Months)")
plt.ylabel("Detection Accuracy (%)")
plt.title("Adaptive Learning Curve of AML System")
plt.grid(True)
plt.legend()
plt.savefig("adaptive_learning_curve.png")