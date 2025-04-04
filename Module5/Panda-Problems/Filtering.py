import pandas as pd

file = pd.read_csv(".\\PyProbs-Updated\\Module5\\Panda-Problems\\company.csv")
df =  pd.DataFrame(file)
df = df.dropna()

filtered_df = df[(df["Department"]=="Sales") & (df["Salary"]>5000)]
print(filtered_df)