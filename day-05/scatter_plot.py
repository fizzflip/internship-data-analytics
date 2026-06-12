from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [10, 20, 30, 40, 50, 60, 70, 80, 92]
plt.scatter(x, y)
plt.xlabel("Hours of Study")
plt.ylabel("Marks Obtained")
plt.grid(True)
plt.show()

internet_usage = [1, 2, 3, 4]
productivity_score = [20, 40, 100, 5]
stress_level = [75, 65, 5, 100]
plt.scatter(internet_usage, productivity_score, s=stress_level)
plt.xlabel("Internet Usage")
plt.ylabel("Productivity Score")
plt.show()
