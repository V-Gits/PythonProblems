import pandas as pd
df = pd.read_csv("employee.csv")
print("First 7 records:\n", df.head(7))

print("\nEmployees in alphabetical order:\n", df["name"].sort_values())

highest_paid = df.loc[df["salary"].idxmax(), "name"]
print("\nEmployee with the highest salary:", highest_paid)

male_employees = df[df["gender"] == "Male"]["name"]
print("\nMale employees:\n", male_employees)

import pandas as pd
df = pd.read_csv("employee.csv")
unique_teams = df["team"].unique()
print("\nTeams employees belong to:", unique_teams)