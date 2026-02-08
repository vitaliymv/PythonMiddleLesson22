import pandas as pd
import os

def performance_label(score: int):
    if score <= 4:
        return "Low"
    elif score <= 8:
        return "Medium"
    return "High"


def add_performance(df:pd.DataFrame, save_path="data/processed/performance_summary.csv"):
    df["Performance"] = df["Score"].apply(performance_label)

    summary = df["Performance"].value_counts().reset_index()
    summary.columns = ["Performance", "Count"]

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df_summary = summary.copy()
    df_summary.to_csv(save_path, index=False)

    print(f"\nPerformance summary saved to {save_path}")
    print(summary)

    return summary
