"""
Script: cost_benefit_analysis_model.py
Purpose: Simulate 5-year cost-benefit analysis for automated AML systems
"""

import numpy as np
import matplotlib.pyplot as plt

years = np.arange(1, 6)
initial_investment = 2.3e6  # $2.3 million
training_cost = 250000
maintenance_annual = 120000
operational_cost_saving = np.array([350000, 550000, 750000, 800000, 850000])
efficiency_gain = np.array([200000, 350000, 500000, 600000, 700000])

total_costs = np.array([initial_investment + training_cost] + [maintenance_annual] * 4)
total_benefits = operational_cost_saving + efficiency_gain

# Net Present Value calculation
discount_rate = 0.08
npv = sum((total_benefits[i] - total_costs[i]) / (1 + discount_rate) ** (i + 1) for i in range(5))

plt.figure(figsize=(10, 6))
plt.bar(years, total_benefits, color='green', label="Benefits")
plt.bar(years, -total_costs, color='red', label="Costs")
plt.axhline(0, color='black')
plt.title("Cost-Benefit Analysis Over 5 Years")
plt.xlabel("Year")
plt.ylabel("USD")
plt.legend()
plt.grid(True)
plt.savefig("cost_benefit_5_years.png")
print(f"Estimated NPV: ${npv:,.2f}")