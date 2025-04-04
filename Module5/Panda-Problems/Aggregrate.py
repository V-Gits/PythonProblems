import pandas as pd

file = pd.read_csv(".\\PyProbs-Updated\\Module5\\Panda-Problems\\company.csv")
df = pd.DataFrame(file)
df = df.dropna()

grouped = df.groupby("Department").agg({
    "Salary": "mean",
    "Age" : "max"
})

print(grouped)