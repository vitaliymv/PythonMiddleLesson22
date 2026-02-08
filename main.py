from src.generate_data import generate_friends_csv, generate_students_csv
from src.load_data import load_csv
from src.basic_stats import calculate_basic_stats
from src.analysis import add_columns, detect_outliers, group_by_city

print("Generate data")
generate_friends_csv()
students_df = generate_students_csv()
print("-" * 20)

print("Task 1")
friends_df = load_csv("data/raw/friends.csv")
calculate_basic_stats(friends_df)
print("-" * 20)

print("Task 2")
print("Average score:", students_df["Score"].mean())
print(students_df["City"].value_counts())
print("-" * 20)

print("Task 3")
students_df = add_columns(students_df)
detect_outliers(students_df)
group_by_city(students_df)


from challenges.challenge import add_performance
add_performance(students_df)

