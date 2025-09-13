# Basic Statistics for Tips Dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("tips.csv")   # make sure tips.csv is in the same folder

# Select 5 important columns
important_cols = [
   "total_bill",
   "tip",
   "size",
   "sex",
   "smoker"
]

# ---- Function to calculate statistics ----
def column_statistics(series):
    stats = {}
    if pd.api.types.is_numeric_dtype(series):
        stats[
   "mean"
] = series.mean()
        stats[
   "median"
] = series.median()
        stats[
   "mode"
] = series.mode()[
   0
]
        stats[
   "min"
] = series.min()
        stats[
   "max"
] = series.max()
        stats[
   "std"
] = series.std()
    else:
        stats[
   "mode"
] = series.mode()[
   0
]
    return stats

# ---- Compute statistics for each column ----
all_stats = {}
for col in important_cols:
    all_stats[col
] = column_statistics(df[col
])

# Display stats
pd.DataFrame(all_stats)

# ---- Graphical Representation for each column ----

for col in important_cols:
    plt.figure(figsize=(10,
4))
    if pd.api.types.is_numeric_dtype(df[col
]):
        # Histogram
        plt.subplot(1,
2,
1)
        sns.histplot(df[col
], kde=True, bins=20, color="skyblue")
        plt.title(f"Histogram of {col}")
        
        # Boxplot
        plt.subplot(1,
2,
2)
        sns.boxplot(y=df[col
], color="orange")
        plt.title(f"Boxplot of {col}")
        
    else:
        # Categorical columns → Countplot
        sns.countplot(x=df[col
], palette="Set2")
        plt.title(f"Countplot of {col}")
    
    plt.tight_layout()
    plt.show()

