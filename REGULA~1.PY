"""
Script: regulatory_compliance_audit_simulation.py
Purpose: Simulate audit scoring under different compliance frameworks
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Mock audit score calculation based on multiple features
def calculate_compliance_score(row):
    score = (
        0.2 * (100 - row["False_Positive_Rate"]) +
        0.3 * row["Detection_Accuracy"] +
        0.2 * row["Scalability_Score"] +
        0.3 * row["Audit_Trail_Score"]
    )
    return round(score, 2)

# Load data
df = pd.read_excel("AML_Efficiency_Dataset.xlsx")
df["Compliance_Score"] = df.apply(calculate_compliance_score, axis=1)

# Plot distribution
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Compliance_Score", hue="Method", kde=True, bins=30)
plt.title("Compliance Score Distribution by Method")
plt.xlabel("Compliance Score")
plt.savefig("compliance_score_distribution.png")