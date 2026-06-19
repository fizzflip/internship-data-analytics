import pandas as pd

data = pd.DataFrame(
    index=["Mahesh", "Ramesh", "Suresh", "Haresh", "Naresh", "Jayesh"],
    columns=["Maths", "English", "Science"],
    data=[[50, 60, 78], [63, 45, 67], [13, 90, 20], [80, 70, 60], [63, 45, 67], [13, 90, 20]]
)

print("--------- Data ---------")
print(data)

print("\n--------- Info ---------")
print(data.info())

print("\n--------- Description ---------")
print(data.describe())

print("\n------------ Shape ------------")
print(data.shape)

print("\n------------ Head ------------")
print(data.head(2))

print("\n------------ Tail ------------")
print(data.tail(2))
