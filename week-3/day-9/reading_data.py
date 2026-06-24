import pandas as pd

# df = pd.read_excel('supermarket-sales-data.xlsx')

df = pd.read_csv("misc/datasets/student-data.csv")

print("\n============ Head ============")
print(df.head())

print("\n============ Tail ============")
print(df.tail())

print("\n============ Shape ============")
print(df.shape)

print("\n============ Column ============")
print(df.columns)

print("\n============ Info ============")
print(df.info())

print("\n============ Describe ============")
print(df.describe())

print("\n============ Accessing Columns ============")
print("Single Columns", df["Maths"])
print("Multiple Columns", df["Name"])

print("\n============ Accessing Rows ============")
print("First Column", df.loc[1])
print("Third Row", df.iloc[3])

print("\n============ Total Marks ============")
df["Total"] = df["Maths"] + df["Science"] + df["English"]
print(df)

print("\n============ Percentage ============(")
df["Percentage"] = round(df["Total"] / 3, 2)
print(df)

print("\n============ Min-Max Marks in Math ============")
print(df["Maths"].max())
print(df["Maths"].min())

print("\n============ Average Marks ============")
print("Maths: ", df["Maths"].mean())
print("Science: ", df["Science"].mean())
print("English: ", df["English"].mean())

print("\n============ Class Topper ============")
topper = df[df["Total"] == df["Total"].max()]
print(topper)

print("\n============ Filtering ============")
print(df[df["Maths"] > 80])
print(df[df["Science"] > 85])

print("\n============ Sorting ============")
print(df.sort_values(by="Total", ascending=False))

print("\n============ Count Students ============")
count = len(df[df["Maths"] > 80])
print(count)

print("\n============ Applying Functions ============")


def grade(per):
    if per >= 90:
        return "A"
    elif per >= 80:
        return "B"
    elif per >= 70:
        return "C"
    else:
        return "D"


df["Grade"] = df["Percentage"].apply(grade)
print(df)

print("\n============ Grade Count ============")
print(df["Grade"].value_counts())

print("\n============ High-Low Percentage ============")
print(df[df["Percentage"] == df["Percentage"].max()])
print(df[df["Percentage"] == df["Percentage"].min()])

df.to_csv("student-data-modified.csv", index=False)
