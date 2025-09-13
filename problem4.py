# Univariate Analysis of 'tip' column

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("tips.csv")   # Ensure tips.csv is in the same folder
df.head()

# Basic statistics
tip_stats = {
    "Mean": df["tip"].mean(),
    "Median": df["tip"].median(),
    "Mode": df["tip"].mode()[0],
    "Min": df["tip"].min(),
    "Max": df["tip"].max(),
    "Standard Deviation": df["tip"].std()
}
tip_stats


plt.figure(figsize=(8,5))
sns.histplot(df["tip"], bins=20, kde=True, color="skyblue")
plt.title("Distribution of Tips (Histogram + KDE)")
plt.xlabel("Tip Amount")
plt.ylabel("Frequency")
plt.show()


plt.figure(figsize=(5,5))
sns.boxplot(y=df["tip"], color="lightgreen")
plt.title("Boxplot of Tips")
plt.ylabel("Tip Amount")
plt.show()


plt.figure(figsize=(5,5))
sns.violinplot(y=df["tip"], color="orange")
plt.title("Violin Plot of Tips")
plt.ylabel("Tip Amount")
plt.show()


print("Univariate Analysis Insights for 'tip':")
print("- The mean tip is around {:.2f}".format(df["tip"].mean()))
print("- The median tip is {:.2f}".format(df["tip"].median()))
print("- The most frequent tip (mode) is {:.2f}".format(df["tip"].mode()[0]))
print("- The minimum tip recorded is {:.2f}, while the maximum is {:.2f}".format(df["tip"].min(), df["tip"].max()))
print("- The standard deviation indicates variability of {:.2f}".format(df["tip"].std()))
