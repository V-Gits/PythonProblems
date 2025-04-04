import pandas as pd

file = pd.read_csv(".\\PyProbs-Updated\\Module5\\Panda-Problems\\company.csv")
df = pd.DataFrame(file)
df = df.dropna()
df["Bonus"] = df["Salary"] * 0.10
df["Salary"] = df["Salary"] * 1.05
print(df)