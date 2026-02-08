import pandas

def calculate_basic_stats(df: pandas.DataFrame, column="Age"):
    mean = df[column].mean()
    median = df[column].median()
    mode = df[column].mode()[0]
    print(f"Mean {column}: {mean}")
    print(f"Median {column}: {median}")
    print(f"Mode {column}: {mode}")
    return mean, median, mode

