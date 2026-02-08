import pandas as pd
from faker import Faker
import os

fake = Faker()

def add_columns(df: pd.DataFrame):
    df["Hours_Study"] = [fake.random_int(1, 5) for _ in range(len(df))]
    df["Projects"] = [fake.random_int(0, 3) for _ in range(len(df))]
    return df

def detect_outliers(df: pd.DataFrame, column="Score"):
    mean_score = df[column].mean()
    std_score = df[column].std()
    outliers = df[df[column] > mean_score + 2 * std_score]
    print("\nOutliers:")
    print(outliers)
    return outliers

def group_by_city(df: pd.DataFrame):
    grouped = df.groupby("City")["Score"].mean().reset_index()
    os.makedirs("data/processed", exist_ok=True)
    grouped.to_csv("data/processed/analysis.csv", index=False)
    print("\nGrouped result saved to analysis.csv")
    print(grouped.head())
    return grouped
