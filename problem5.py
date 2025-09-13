# Bivariate Analysis of Tips vs Gender

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("tips.csv")   # Ensure tips.csv is in the same folder
df.head()

# Group by gender and compute basic stats
gender_stats = df.groupby("sex")["tip"].agg(["count", "mean", "median", "std", "min", "max"])
gender_stats

plt.figure(figsize=(6,5))
sns.boxplot(x="sex", y="tip", data=df, palette="pastel")
plt.title("Boxplot of Tips by Gender")
plt.xlabel("Gender")
plt.ylabel("Tip Amount")
plt.show()

plt.figure(figsize=(6,5))
sns.violinplot(x="sex", y="tip", data=df, palette="muted")
plt.title("Violin Plot of Tips by Gender")
plt.xlabel("Gender")
plt.ylabel("Tip Amount")
plt.show()

plt.figure(figsize=(6,5))
sns.barplot(x="sex", y="tip", data=df, estimator="mean", ci="sd", palette="Set2")
plt.title("Average Tip by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Tip Amount")
plt.show()

print("Bivariate Analysis Insights (Tips vs Gender):")
print("- Males and Females may have different tipping behaviors.")
print("- Check mean values from the grouped statistics to see who tips more on average.")
print("- Boxplot & violin plots show spread and skewness of tip distribution.")
print("- Barplot highlights the average tip difference clearly.")

