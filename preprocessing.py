import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("Warehouse_and_Retail_Sales.csv")

df.columns = df.columns.str.strip()

# PART 1: DATA PREPROCESSING

df['DATE'] = pd.to_datetime(df['YEAR'].astype(str) + '-' + df['MONTH'].astype(str))

# Drop rows with missing or invalid sales
df = df[df['RETAIL SALES'].notna()]
df = df[df['RETAIL SALES'] >= 0]  # Assumption: Negative values are data errors

# Group by DATE for time-series trend
monthly_sales = df.groupby('DATE')['RETAIL SALES'].sum().reset_index()

# Plot Monthly Retail Sales Trend
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='DATE', y='RETAIL SALES', marker='o')
plt.title("Figure 1: Monthly Retail Sales Trend")
plt.ylabel("Total Retail Sales")
plt.xlabel("Date")
plt.grid(True)
plt.tight_layout()
plt.show()

# PART 2: LLN & CLT DEMONSTRATION

# A. Law of Large Numbers (LLN)
overall_mean = df['RETAIL SALES'].mean()
sample_means = []

# Draw 1000 random samples of size 100
for _ in range(1000):
    sample = df['RETAIL SALES'].sample(n=100, replace=True)
    sample_means.append(sample.mean())

# Print comparison
print(f"Population Mean: {overall_mean:.2f}")
print(f"Average of Sample Means: {np.mean(sample_means):.2f}")

# B. Central Limit Theorem (CLT)
plt.figure(figsize=(10, 5))
sns.histplot(sample_means, bins=30, kde=True, color='skyblue')
plt.axvline(overall_mean, color='red', linestyle='--', label='Population Mean')
plt.title("Figure 2: CLT - Distribution of Sample Means (n=100)")
plt.xlabel("Sample Mean of Retail Sales")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
