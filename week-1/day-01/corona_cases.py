# lvl1 data
corona_cases = {
    "ahemdabad": 8500,
    "rajkot": 6500,
    "bhavnagar": 9600
}

print(f"Rajkot {corona_cases['rajkot']}")

# lvl2 data
corona_cases_2 = {
    "ahemdabad": [3000, 1500, 4000],
    "rajkot": [2000, 3000, 1500],
    "bhavnagar": [1000, 2000, 1400]
}

print(f"Rajkot recovered cases are: {corona_cases_2['rajkot'](1)}")

# lvl2 data
corona_cases_3 = {
    "ahemdabad": [3000, 1500, 4000],
    "rajkot": [
        {
            'date': '02-06-2020',
            'cases': 2000
        },
        {
            'date': '03-06-2020',
            'cases': 4000
        }
    ],
    "bhavnagar": [1000, 2000, 1400]
}

print(corona_cases_3)
