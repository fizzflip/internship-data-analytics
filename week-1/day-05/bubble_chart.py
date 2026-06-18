from matplotlib import pyplot as plt

days_worked = [1, 2, 3, 4, 5, 6, 7]
hours_per_day = [8, 9, 8, 10, 12, 6, 4]
stress_levels = [50, 60, 55, 80, 100, 40, 20]

plt.scatter(days_worked, hours_per_day, s=stress_levels, alpha=0.5)
plt.xlabel("Days Worked")
plt.ylabel("Hours per Day")
plt.title("Work Habits and Stress Levels (Bubble Chart)")
plt.grid(True)
plt.show()
