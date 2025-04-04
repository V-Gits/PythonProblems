import pandas as pd 

data = {
    "Name": ["Tom", "nick", "krish", "jack"],
    "Age": [20, 21, 19, 18],
    "Department": ["Sales", "Marketing", "Sales", "HR"],
    "Salary": [5000, 6000, 7000, 8000]
}
df = pd.DataFrame(data)
filename = "company.csv"
df.to_csv(filename, index=False)
print(df)