# Missing Values & Outlier Detection in Tips Dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("tips.csv")   # Ensure tips.csv is in the same folder
df.head()

# Check for missing values
print("Missing values per column:")
print(df.isnull().sum())

# Visualize missing values (heatmap)
plt.figure(figsize=(8,5))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")
plt.show()

# Plot boxplots for numeric columns
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

plt.figure(figsize=(15,5))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(1, len(numeric_cols), i)
    sns.boxplot(y=df[col], color="lightblue")
    plt.title(f"Boxplot of {col}")
plt.tight_layout()
plt.show()


# IQR method to detect outliers
def find_outliers_iqr(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return series[(series < lower_bound) | (series > upper_bound)]

# Apply for all numeric columns
outliers = {}
for col in numeric_cols:
    outliers[col] = find_outliers_iqr(df[col])

outliers


