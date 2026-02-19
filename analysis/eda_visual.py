import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.analysis import add_columns

df = pd.read_csv("../data/raw/students.csv")
df = add_columns(df)

df["Efficiency"] = df["Score"] / df["Hours_Study"]

sns.set(style="whitegrid")

plt.figure()
sns.histplot(df["Score"], kde=True)
plt.title("Score Distribution")
plt.show()

# 2. Boxplot Hours_Study vs Score
plt.figure()
sns.boxplot(x="Hours_Study", y="Score", data=df)
plt.title("Score Distribution by Hours_Study")
plt.show()

# 3. Violin plot Projects vs Score
plt.figure()
sns.violinplot(x="Projects", y="Score", data=df)
plt.title("Score Distribution by Projects")
plt.show()

# 4. Barplot Average Score by Projects
plt.figure()
sns.barplot(x="Projects", y="Score", data=df)
plt.title("Average Score by Projects")
plt.show()

# 5. Heatmap для числових колонок
numeric_df = df.select_dtypes(include="number")
plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# 6. Barplot — кількість студентів по Performance
perf_df = pd.read_csv(
    "../data/processed/performance_summary.csv"
)
plt.figure()
sns.barplot(x="Performance", y="Count", data=perf_df)
plt.title("Number of Students by Performance")
plt.show()
