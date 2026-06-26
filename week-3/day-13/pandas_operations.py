import pandas as pd

data = {
    "name": ["Amit", "Neha", "Raj"],
    "age": [21, 22, 20],
    "marks": [85, 90, 78]
}

df = pd.DataFrame(data)
print(df)

name = input("Name: ")
age = int(input("Age: "))
marks = int(input("Marks: "))

new_row = {
    "name": name,
    "age": age,
    "marks": marks
}

df.loc[len(df)] = new_row
print(df)
