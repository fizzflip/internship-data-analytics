import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
stock_price = [100, 120, 130, 122, 105]
stock_price_2 = [45, 50, 56, 52, 57]

plt.fill_between(days, stock_price, alpha=0.5, color='red')
plt.fill_between(days, stock_price_2, alpha=0.5, color='blue')
plt.plot(days, stock_price_2)
plt.plot(days, stock_price)

plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.title('Stock Trend')
plt.show()
