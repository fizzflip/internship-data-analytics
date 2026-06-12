import matplotlib.pyplot as plt

salary = [14_000, 15_000, 21_000, 25_000, 30_000,
          37_000, 35_000, 44_000, 45_000, 50_000,
          54_000, 64_000, 65_000, 73_000, 75_000,
          80_000, 85_000, 90_000, 95_000, 1_00_000]

plt.hist(salary, edgecolor="black", color="red", bins=50)
plt.show()

data = {"sales": [100, 200, 300, 400, 500, 600, 700, 800, 900]}
plt.hist(data["sales"], edgecolor="black", color="red", bins=50)
plt.show()
