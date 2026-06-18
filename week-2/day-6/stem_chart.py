import matplotlib.pyplot as plt

time = ["9:00", "10:00", "11:00", "12:00", "13:00"]
orders = [10, 15, 26, 45, 87]

plt.stem(time, orders)
plt.xlabel('Time')
plt.ylabel('Orders')
plt.title('Time Wise Order')
plt.grid(True)
plt.show()
