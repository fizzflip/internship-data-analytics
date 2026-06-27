import pandas as pd

data = {
    "name": ["Amit", "Mohit", "Sumit", "Rohan"],
    "dept": ["IT", "HR", "IT", "HR"],
    "sal": [50_000, 40_000, 60_000, 55_000],
}

df = pd.DataFrame(data)
result = df.groupby("dept")["sal"].sum()
print(result)

result = df.groupby("dept")["sal"].agg(["sum", "mean", "max"])
print(result)
