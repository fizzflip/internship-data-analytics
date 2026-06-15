import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
temp_ahmd = [35, 37, 36, 32, 31, 33, 35]
temp_surt = [29, 37, 33, 30, 39, 39, 27]
temp_rajk = [45, 35, 37, 20, 36, 39, 17]

plt.plot(days, temp_ahmd, label="Ahmd", marker="o", linestyle="--")
plt.plot(days, temp_surt, label="Surt", marker="*", linestyle=":")
plt.plot(days, temp_rajk, label="Rajk", marker="^", linestyle="-.")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Temperature Trend")
plt.legend()
plt.grid(True)
plt.show()
