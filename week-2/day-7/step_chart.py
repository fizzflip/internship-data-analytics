import matplotlib.pyplot as plt

stock_days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
stock_price = [120, 150, 145, 132, 164]

plt.step(stock_days, stock_price, where='post', label='Stock Price')
plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.title('Price Trend')
plt.show()
