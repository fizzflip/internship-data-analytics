import pandas as pd

# python data structures - series

lst = [10, 20, 30, 40, 50]
print(lst)

ser = pd.Series(lst)
print(ser)

dict_data = {
    "name": ["Rohit", "Gill", "Hardik"],
    "type": ["Batsman", "Batsman", "All-Rounder"],
    "runs": [10_000, 9000, 4500]
}

df = pd.DataFrame(dict_data)
print(df)

df = pd.DataFrame([
    [14_500, 21_054, 2051],
    [10, 55, 120],
    [145, 175, 51],
    ["Wicket-Keeper", "Batsman", "Bowler"]
], columns=["Adb", "Gayle", "Warner"],
    index=["Runs", "Wickets", "Highest", "Type"]
)
print(df)
