import pandas as pd
import requests

url = "https://api.tvmaze.com/search/shows"

show = input("Show Name: ").lower()
parameters = {"q": show}

response = requests.get(url, params=parameters)
data = response.json()

df = pd.json_normalize(data)
print(df)
