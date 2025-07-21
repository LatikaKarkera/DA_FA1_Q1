import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv("Warehouse_and_Retail_Sales.csv")

# Step 1: Basic Cleaning
df.columns = df.columns.str.strip()  # Remove extra spaces
df.dropna(subset=['RETAIL SALES'], inplace=True)  # Drop rows where sales are missing

# Step 2: Convert YEAR and MONTH to datetime
df['DATE'] = pd.to_datetime(df['YEAR'].astype(str) + '-' + df['MONTH'].astype(str))

# Step 3: Aggregate Monthly Sales
monthly_sales = df.groupby('DATE')['RETAIL SALES'].sum().reset_index()

# Plot Monthly Sales Trend
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='DATE', y='RETAIL SALES', marker='o')
plt.title("Monthly Retail Sales Trend")
plt.ylabel("Total Retail Sales")
plt.xlabel("Date")
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 4: Law of Large Numbers Demo
sample_means = []
for i in range(1000):
    sample = df['RETAIL SALES'].sample(n=100, replace=True)
    sample_means.append(sample.mean())

print(f"Average of Sample Means: {np.mean(sample_means):.2f}")
print(f"Overall Mean: {df['RETAIL SALES'].mean():.2f}")

# Step 5: Central Limit Theorem Demonstration
plt.figure(figsize=(10, 5))
sns.histplot(sample_means, bins=30, kde=True, color='orange')
plt.title("CLT Demonstration: Sampling Distribution of the Mean (n=100)")
plt.xlabel("Sample Mean of Retail Sales")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()