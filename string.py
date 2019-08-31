# String in the Python are surrounded by either single or double quotation mark.

name = 'Awanish'
age  = 32

# Concation of string

print('Hello World.')

print('Hello I am ' + name + ' I am ' + str(age))

# String formatting

# Argument by position

print('{}, {}, {}'.format('a', 'b', 'c'))

print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by name

#print('My name is {name} and my age is {age}'.format(name = name, age = age))

# F-string supporting version (3.6 +)

print(f'My name is {name} and my age is {age}')

# String methods

s = 'hello world there'

# Capitalize first letter

print(s.capitalize())

# Swap Case
print(s.swapcase())

# Get lenght

print(len(s))

# Replacements

print(s.replace('world', 'everyone'))

