import pandas as pd

df = pd.read_csv("../data/raw/students.csv")

print("=== INFO ===")
print(df.info())

print("\n=== DESCRIBE ===")
print(df.describe())

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())
