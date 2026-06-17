import matplotlib.pyplot as plt

month = ["jan-feb", "mar-apr", "may-jun", "jul-aug", "sept-oct", "nov-dev"]
ac = [120, 140, 240, 300, 120, 100]
tv = [100, 110, 90, 95, 120, 110]
fridge = [400, 500, 456, 500, 560, 600]

plt.stackplot(month, ac, tv, fridge, labels=["AC", "TV", "Fridge"])
plt.xlabel('Month')
plt.ylabel('Amount')
plt.legend()
plt.title('Stacked Plot')
plt.show()
