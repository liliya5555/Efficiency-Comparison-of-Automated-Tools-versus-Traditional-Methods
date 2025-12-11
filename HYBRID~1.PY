"""
Script: hybrid_model_decision_tree.py
Purpose: Build a decision tree to determine when to use manual review over automation
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("AML_Efficiency_Dataset.xlsx")

# Create target: 1 = Manual review recommended, 0 = Automation sufficient
df["Manual_Review_Required"] = ((df["False_Positive_Rate"] > 20) | (df["Detection_Accuracy"] < 75)).astype(int)

# Features and model
features = ["Transactions_per_Hour", "Detection_Accuracy", "False_Positive_Rate", "Scalability_Score"]
X = df[features]
y = df["Manual_Review_Required"]

clf = DecisionTreeClassifier(max_depth=4, random_state=42)
clf.fit(X, y)

# Plot tree
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=features, class_names=["Automation", "Manual"], filled=True)
plt.title("Hybrid Model Decision Tree")
plt.savefig("hybrid_model_decision_tree.png")