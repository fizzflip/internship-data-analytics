import requests

json_data = requests.get('https://api.coinlore.net/api/tickers/').json()

coin_found = False
user_coin = input("Coin: ")
for coin in json_data['data']:
    if coin['name'] == user_coin:
        print("Price is " + coin['price_usd'])
        coin_found = True

if not coin_found:
    print("Coin not found!")