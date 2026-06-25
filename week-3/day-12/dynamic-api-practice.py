import requests

url = "http://universities.hipolabs.com/search"

country = input("Country Name: ").lower()
parameters = {"country": country}

response = requests.get(url, params=parameters)
data = response.json()

print(f"Found {len(data)} universities.")
