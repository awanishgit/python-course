# A Dictionary is a collection which is unordered, changable, and indexed.
# No duplicate member

# Simple dictionary

person = {
    'first_name': 'Awanish',
    'last_name': 'Pandey',
    'age': 31
}

# person = dict(first_name = 'Awanish', last_name = 'pandey', age = 31)

# Accessing single value

# print(person['first_name'])

# print(person.get('last_name'))

# Add key/value

person['phone'] = '111-111-111'

# Get keys

# print(person.keys())

# Get items

# print(person.items())

# Make copy of dictionary

person2 = person.copy()

person2['city'] = 'New Delhi'

# Removing items

del person['age']
person.pop('phone')

# Clear the dictionary

# person.clear()

# Get length

print(len(person2))

# List of dictionary

people = [
    {'name': 'Ravi', 'age': 25},
    {'name': 'Gyan', 'age': 34}
]

people2 = [
    person
]
print(people2)
# print(person2)

print(person)