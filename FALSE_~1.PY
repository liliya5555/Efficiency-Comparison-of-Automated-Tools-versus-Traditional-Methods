"""
Script: false_positive_analysis_with_confidence.py
Purpose: Analyze false positive rates and calculate confidence intervals
"""

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("AML_Efficiency_Dataset.xlsx")

# Function to calculate confidence interval
def confidence_interval(data, confidence=0.95):
    mean = np.mean(data)
    sem = stats.sem(data)
    h = sem * stats.t.ppf((1 + confidence) / 2., len(data)-1)
    return mean, mean-h, mean+h

methods = df["Method"].unique()
results = []

for method in methods:
    method_data = df[df["Method"] == method]["False_Positive_Rate"]
    mean, lower, upper = confidence_interval(method_data)
    results.append((method, mean, lower, upper))

# Convert to DataFrame and plot
ci_df = pd.DataFrame(results, columns=["Method", "Mean", "Lower", "Upper"])

plt.figure(figsize=(8, 6))
plt.errorbar(ci_df["Method"], ci_df["Mean"], yerr=[ci_df["Mean"] - ci_df["Lower"], ci_df["Upper"] - ci_df["Mean"]], fmt='o', capsize=5)
plt.title("False Positive Rate with 95% Confidence Interval")
plt.ylabel("False Positive Rate (%)")
plt.grid(True)
plt.savefig("false_positive_confidence.png")