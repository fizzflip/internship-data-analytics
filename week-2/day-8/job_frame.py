import pandas as pd

df = pd.DataFrame(
    index=["ABC", "XYZ"],
    columns=[2023, 2024, 2025],
    data=[
        [21_000, 22_000, 23_000],
        [28_000, 29_000, 35_000]
    ]
)

print(df)

df[2026] = df[2025] * 1.12
print(df)

df["total"] = 12 * (df[2023] + df[2024] + df[2025] + df[2026])
print(df)
