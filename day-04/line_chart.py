import matplotlib.pyplot as plt

# Line - I
days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
stock_price = [12, 34, 12, 3, 45]
plt.plot(days, stock_price)
plt.xlabel("Days")
plt.ylabel("Price")
plt.title("Stock Price")
plt.show()

# Line - II
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12_000, 23_000, 10_000, 17_000, 25_000, 19_000]
plt.plot(months, sales, color="blue")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Distribution")
plt.show()
