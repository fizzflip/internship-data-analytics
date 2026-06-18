import matplotlib.pyplot as plt

it_salary = [20_000, 50_000, 30_000, 40_000, 1_20_000]
hr_salary = [10_000, 20_000, 35_000, 45_000, 55_000]
sales_salary = [10_000, 15_000, 20_000, 35_000, 45_000]

data = [it_salary, hr_salary, sales_salary]

plt.boxplot(data)
plt.xlabel('Department')
plt.ylabel('Salary')
plt.xticks([1, 2, 3], ["IT", "HR", "Sales"])
plt.show()
