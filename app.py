import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from analysis.recommendation import generate_recommendation

st.set_page_config(page_title="Student Segmentation", layout="wide")
st.title("🎓 Student Segmentation & Recommendation System")

df = pd.read_csv("data/processed/students_with_features.csv")

st.subheader("Dataset preview")
st.dataframe(df.head())

features = df[["Hours_Study", "Projects", "Score", "Efficiency"]]

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(features_scaled)

cluster_means = df.groupby("Cluster")["Score"].mean().sort_values()
cluster_mapping = {
    cluster_means.index[0]: "Low",
    cluster_means.index[1]: "Medium",
    cluster_means.index[2]: "High"
}
df["Cluster_Label"] = df["Cluster"].map(cluster_mapping)

st.subheader("📊 Dataset Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Students", len(df))
col2.metric("Average Score", round(df["Score"].mean(), 2))
col3.metric("Average Efficiency", round(df["Efficiency"].mean(), 2))

st.subheader("📈 Segmentation Visualization")
fig, ax = plt.subplots()
sns.scatterplot(
    x="Hours_Study",
    y="Score",
    hue="Cluster_Label",
    data=df,
    palette="Set2",
    ax=ax
)
ax.set_title("Hours Study vs Score (Clusters)")
st.pyplot(fig)

st.subheader("📊 Cluster Summary (Mean Values)")
cluster_summary = df.groupby("Cluster_Label")[
    ["Score", "Hours_Study", "Projects", "Efficiency"]
].mean().round(2)
st.dataframe(cluster_summary)

if "Performance" in df.columns:
    st.subheader("📊 Cluster vs Performance")
    st.dataframe(pd.crosstab(df["Cluster_Label"], df["Performance"]))

st.subheader("🔎 Analyze New Student")
hours = st.slider("Hours Study", 1, 10, 3)
projects = st.slider("Projects", 0, 5, 1)
score = st.slider("Score", 1, 10, 6)

if st.button("Analyze Student"):
    efficiency = score / hours
    new_student = pd.DataFrame({
        "Hours_Study": [hours],
        "Projects": [projects],
        "Score": [score],
        "Efficiency": [efficiency]
    })

    new_scaled = scaler.transform(new_student)
    cluster_num = kmeans.predict(new_scaled)[0]
    cluster_label = cluster_mapping[cluster_num]

    recommendation = generate_recommendation(cluster_label, score)

    st.success(f"Assigned Cluster: {cluster_label}")
    st.info(f"Recommendation: {recommendation}")