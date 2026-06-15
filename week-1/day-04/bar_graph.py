# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

# Bar Graph - I
car_brands = ["Audi", "Toyota", "BMW", "Tesla", "Tata"]
car_sales = [100, 200, 300, 400, 500]
plt.bar(car_brands, car_sales, color="red")
plt.xlabel("Brands")
plt.ylabel("Sales")
plt.title("Sales vs Brand")
plt.show()

# Bar Graph - II
players = ["Vaibhav", "Jadeja", "Dhoni", "Kholi", "Shubhman"]
runs = [780, 300, 100, 600, 800]
plt.bar(players, runs, color=["red", "green", "blue", "cyan", "magenta"])
plt.xlabel("Players")
plt.ylabel("Runs")
plt.title("Runs vs Player")
plt.show()

# Bar Graph - III
data = {"Ramesh": 90, "Mahesh": 49, "Naresh": 67, "Haresh": 23}
plt.bar(data.keys(), data.values())
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks vs Students")
plt.show()
