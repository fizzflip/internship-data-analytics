import matplotlib.pyplot as plt

# Pie Chart - I
salary_dist = [15_000, 20_000, 30_000, 10_000]
salary_dist_category = ["Food", "Healthcare", "Savings", "Investment"]
plt.pie(salary_dist, labels=salary_dist_category, autopct="%1.1f%%")
plt.title("Salary Distribution")
plt.show()

# Pie Chart - II
stocks = ["Tata", "Adani", "Apple", "ICICI"]
market = [20, 10, 40, 30]
plt.pie(market, labels=stocks, autopct="%1.1f%%", colors=["red", "green", "blue", "yellow"])
plt.title("Stock Distribution")
plt.show()
