import requests

url = "https://api.postalpincode.in/pincode/393030"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    print(data)

except requests.exceptions.ConnectionError:
    print("Error: The connection was aborted by the remote server.")
except Exception as e:
    print(f"An error occurred: {e}")
