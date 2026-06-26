import numpy as np
import pandas as pd

df = pd.read_csv('misc/datasets/ecommerce-orders.csv')

print("\n============= Initial Observations =============")
print(df, '\n')
print(df.info())

print("\n============ Missing Values ============")
print(df.isnull().sum())

print("\n============ Coerce Values ============")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
print(df[["Price", "Quantity", "Rating"]])

print("\n============ Absolute Values ============")
df["Price"] = df["Price"].map(lambda x: abs(x))
df["Quantity"] = df["Quantity"].map(lambda x: abs(x))
print(df[["Price", "Quantity"]])

print("\n============ Drop Outliers ============")
df.loc[df["Rating"] > 5, "Rating"] = np.nan
print(df["Rating"])

print("\n============= Approx Values =============")
mean_price = round(df["Price"].mean(), 2)
mean_rating = round(df["Rating"].mean(), 2)
median_quantity = round(df["Quantity"].median(), 2)

print(f"""
Mean Price: {mean_price}
Mean Rating: {mean_rating}
Median Quantity: {median_quantity}""")

print("\n============= Eliminate NaN =============")
df.fillna({"Quantity": median_quantity}, inplace=True)
df.fillna({"Rating": mean_rating}, inplace=True)
df.fillna({"Price": mean_price}, inplace=True)
print(df[["Price", "Quantity", "Rating"]])

print("\n============= Fix Outliers =============")
df.loc[df["Quantity"] == 0, "Quantity"] = 1
df.loc[df["Price"] == 0, "Price"] = mean_price
print(df[["Price", "Quantity"]])

print("\n============= Change Data Types =============")
df["Price"] = df["Price"].astype(float)
df["Rating"] = df["Rating"].astype(float)
df["Quantity"] = df["Quantity"].astype(int)
print(df.info())

print("\n============= Total Amount =============")
df["total_amount"] = df["Price"] * df["Quantity"]
print(df["total_amount"])
print("Total Revenue:", round(df["total_amount"].sum(), 2))

print("\n============= Value Flag =============")
df["high_value_order"] = df["total_amount"] > 20_000
print(df.head(5))

df.to_csv('ecommerce-orders-cleaned.csv', index=False)
print("\necommerce-orders-cleaned.csv written successfully")
