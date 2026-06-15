import requests

url = 'https://api.coinlore.net/api/tickers/'
data = requests.get(url)
json_data = data.json()

print("", json_data['data'][0]['price_usd'])

for coin in json_data['data']:
    print(coin['name'], coin['price_usd'])