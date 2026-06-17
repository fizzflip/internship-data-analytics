import matplotlib.pyplot as plt

weekdays_sleep_hours = [8, 9, 11, 5]
weekdays_phone_usage = [7, 8, 10, 11]

weekend_sleep_hours = [12, 13, 11, 10]
weekend_phone_usage = [10, 11, 8, 9]

plt.scatter(weekdays_sleep_hours, weekdays_phone_usage, color='blue', label='weekdays')
plt.scatter(weekend_sleep_hours, weekend_phone_usage, color='red', label='weekends')
plt.ylabel('Sleep Hours')
plt.xlabel('Phone Usage')
plt.legend()
plt.title('Sleep Hours vs Phone Usage')
plt.grid(True)
plt.show()
