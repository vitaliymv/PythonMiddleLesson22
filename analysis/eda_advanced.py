import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.analysis import add_columns
from challenges.challenge import add_performance

df = pd.read_csv("../data/raw/students.csv")
df = add_columns(df)
summary = add_performance(df)
df["Efficiency"] = df["Score"] / df["Hours_Study"]

numeric_df = df.select_dtypes(include="number")

print("\n=== CORRELATION WITH SCORE ===")
print(numeric_df.corr()["Score"].sort_values(ascending=False))

plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

plt.figure()
sns.histplot(df["Efficiency"], kde=True)
plt.title("Efficiency Distribution")
plt.show()

plt.figure()
sns.boxplot(x="Performance", y="Efficiency", data=df)
plt.title("Efficiency by Performance")
plt.show()
