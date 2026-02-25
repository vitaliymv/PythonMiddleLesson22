import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analysis.segmentation import (
    prepare_features,
    scale_features,
    find_optimal_k,
    apply_kmeans
)
from analysis.recommendation import generate_recommendation

df = pd.read_csv("data/processed/students_with_features.csv")
features = prepare_features(df)

features_scaled = scale_features(features)

inertia = find_optimal_k(features_scaled)

plt.figure()
plt.plot(range(1, 8), inertia)
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.show()

df, model = apply_kmeans(
    df,
    features_scaled,
    n_clusters=3
)

plt.figure()
sns.scatterplot(
    x="Hours_Study",
    y="Score",
    hue="Cluster",
    data=df,
    palette="Set2"
)
plt.title("Student Segmentation (Hours vs Score)")
plt.show()

if "Performance" in df.columns:
    print("\nCluster vs Performance:")
    print(pd.crosstab(df["Cluster"], df["Performance"]))

df["Recommendation"] = df["Cluster"].apply(
    generate_recommendation
)

print("\nSample with Recommendations:")
print(df[
          [
              "Score",
              "Hours_Study",
              "Cluster",
              "Recommendation"
          ]
      ].head())

print("\nCluster Profiles:")
cluster_profile = df.groupby("Cluster")[
    ["Score", "Hours_Study", "Projects", "Efficiency"]
].mean()

print(cluster_profile)
segmented_path = "data/processed/students_segmented.csv"
df.to_csv(segmented_path, index=False)
print(f"\nSegmented data saved to {segmented_path}")