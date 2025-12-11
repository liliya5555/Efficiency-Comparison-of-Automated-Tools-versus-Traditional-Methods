"""
Script: anomaly_detection_unsupervised_model.py
Purpose: Use unsupervised learning to detect anomalies in AML metrics
"""

import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_excel("AML_Efficiency_Dataset.xlsx")

features = ["Transactions_per_Hour", "Detection_Accuracy", "False_Positive_Rate", "Cost_per_Transaction"]
X = df[features]

# Isolation Forest
iso = IsolationForest(contamination=0.03, random_state=42)
df["Anomaly_Score"] = iso.fit_predict(X)

# Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Detection_Accuracy", y="False_Positive_Rate", hue="Anomaly_Score", palette={1: "blue", -1: "red"})
plt.title("Anomaly Detection in AML Performance Metrics")
plt.savefig("anomaly_detection_iforest.png")