import requests

url = 'https://api.mfapi.in/mf'
json_data = requests.get(url).json()

print(f"No. of Mutual Funds: {len(json_data)}")

for fund in json_data:
    print(f"{fund['schemeCode']} | {fund['schemeName']}")

found = False
user_scheme_code = int(input("Enter Scheme Code: "))
for fund in json_data:
    if user_scheme_code == fund['schemeCode']:
        print("Scheme:", fund['schemeName'])
        found = True
        break

if not found:
    print("Invalid Scheme Code")