# JSON is commonly used with data APIs. Here how we can parse JSON into Python dictionary

import json

# Sample json

userJson = '{"first_name": "Awanish", "last_name": "Pandey", "age": "30"}'

# Parse to dictionary

user = json.loads(userJson)
print(user)
print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1980}
carJson = json.dumps(car)
print(carJson)