import requests

api_response = requests.get('https://isro.vercel.app/api/spacecrafts')
json_data = api_response.json()

print(json_data)

# Count number of spacecrafts
spacecraft_count = len(json_data)
print(spacecraft_count)

spacecrafts = json_data['spacecrafts']

for spacecraft in spacecrafts:
    print("Spacecraft:", spacecraft['name'])

# Get spacecraft name based on user input (ID)
user_input_id = input("ID: ")

found = False
for spacecraft in spacecrafts:
    if spacecraft['id'] == user_input_id:
        print("Spacecraft name: ", spacecraft['name'])
        found = True

if not found:
    print("Spacecraft not found")
