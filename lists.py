# A list is a collection which is ordered and changable. Allows duplicate memebers.

# Create List

# number = [1,2,3,4,5]

# Using constructor

number = list((1,2,3,4,5))

fruits = ['Apple', 'Oranges', 'Banana', 'Pear', 10]

print(fruits)

# Get Value of an index

print(fruits[1])

# Get length

print(len(fruits))

# Append in list

fruits.append('Mangoes')

print(fruits)

fruits.remove('Oranges')

# Insert into position

fruits.insert(2, 'Cherry')

print(fruits)

# Remove from position

fruits.pop(4)

print(fruits)

# Reverse list

fruits.reverse()

print(fruits)

# Sorting list

fruits.sort()

print(fruits)

# Reverse sorting

fruits.sort(reverse = True)

print(fruits)

# Change Value

fruits[1] = 'Strawberry'

print(fruits)