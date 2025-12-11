"""
Script: automated_vs_manual_efficiency_analysis.py
Purpose: Compare processing speed and detection accuracy between traditional and automated AML systems
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("AML_Efficiency_Dataset.xlsx")

# Summary statistics
summary = df.groupby("Method")[["Transactions_per_Hour", "Detection_Accuracy"]].mean()

# Visualization
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="Method", y="Transactions_per_Hour", ci="sd")
plt.title("Transaction Processing Speed Comparison")
plt.ylabel("Transactions per Hour")
plt.savefig("processing_speed_comparison.png")
plt.close()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Method", y="Detection_Accuracy")
plt.title("Detection Accuracy Comparison")
plt.ylabel("Accuracy (%)")
plt.savefig("detection_accuracy_comparison.png")
plt.close()