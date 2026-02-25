import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

def prepare_features(df: pd.DataFrame):
    df["Efficiency"] = df["Score"] / df["Hours_Study"]
    features = df[
        [
            "Hours_Study",
            "Projects",
            "Score",
            "Efficiency"
        ]
    ]
    return features

def scale_features(features: pd.DataFrame):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)
    return scaled

def find_optimal_k(features_scaled):
    inertia = []
    for k in range(1, 8):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(features_scaled)
        inertia.append(kmeans.inertia_)

    return inertia

def apply_kmeans(df: pd.DataFrame, features_scaled, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df["Cluster"] = kmeans.fit_predict(features_scaled)

    score = silhouette_score(features_scaled, df["Cluster"])
    print(f"Silhouette Score: {score:.3f}")

    return df, kmeans