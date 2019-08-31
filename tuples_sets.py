# A Tuple is a collection which is ordered and unchangable. Allow duplicate members.

# Simeple Tuple

fruitsTuple = ('Apple', 'Oranges', 'Mangoes')

# Using constructor

# fruitsTuple = tuple(('Apple', 'Oranges', 'Mangoes'))

# Get single value

# print(fruitsTuple[1])

# Cannot change value

# fruitsTuple[1] = 'Grapes'

# print(fruitsTuple)

# Tuples with one value should have trailing comma otherwise it print the value only

fruitsTuple2 = ('Apple',)

# Delete tuple

# del fruitsTuple2

# print(fruitsTuple2)

# Get length of tuple

# print(len(fruitsTuple))


# A Set is a collection which is unordered and unindexed. No duplicate members


# Create Set

fruitSet = {'Apple', 'Oranges', 'Mangoes'}

# Check if in list

# print('Apples' in fruitSet)

# Adding to set 

fruitSet.add('Grape')

# Removing from set 

fruitSet.remove('Grape')

# Clear set 

# fruitSet.clear()

# Deleting set

# del fruitSet

print(fruitSet)

