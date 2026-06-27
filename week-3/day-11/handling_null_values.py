import numpy as np
import pandas as pd

data = {
    "name": ["Ramesh", "Mahesh", "Suresh", "Satish", "Harsh"],
    "marks": [80, np.nan, 90, np.nan, np.nan],
}

df = pd.DataFrame(data)
print(df)

print(df.dropna())
print(df)

print(df.fillna(10))
print(df)

df = df.fillna(-1)
print(df)
