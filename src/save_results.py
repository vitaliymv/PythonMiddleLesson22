import pandas as pd
import os

def save_csv(df: pd.DataFrame, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Saved data to {path}")
