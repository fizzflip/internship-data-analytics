import matplotlib.pyplot as plt

teenage = [12, 24, 13, 15, 17]
young_adult = [120, 150, 160, 170, 110]
middle_aged = [10, 15, 7, 8, 13]

data = [teenage, young_adult, middle_aged]

plt.violinplot(data)
plt.xlabel('Age Group')
plt.ylabel('Time for Music')
plt.xticks([1, 2, 3], ["Teenagers", "Young Adults", "Middle Aged"])
plt.show()
