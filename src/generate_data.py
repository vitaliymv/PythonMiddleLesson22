import pandas as pd
from faker import Faker
import random
import os

fake = Faker()

def generate_friends_csv(path="data/raw/friends.csv"):
    fruits = ["Apple", "Banana", "Orange", "Kiwi", "Mango"]
    data = []

    for _ in range(20):
        data.append({
            "Name": fake.first_name(),
            "Age": random.randint(18, 30),
            "Favorite_Fruit": random.choice(fruits)
        })

    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Friends data saved to {path}")

def generate_students_csv(path="data/raw/students.csv", n=10000):
    data = []

    for _ in range(n):
        data.append({
            "Name": fake.first_name(),
            "Age": fake.random_int(10, 18),
            "City": fake.city(),
            "Score": fake.random_int(1, 12)
        })

    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Students data saved to {path}")
    return df

