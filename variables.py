# A variable is a container for value which can be various types

'''
This is a 
example of multiline
comment

'''

"""
Variable Rules:

    - Variable names are case sensitives
    - Must start with a letter or an underscore
    - Can have number but not start with one
"""

# x = 1                   # int
# y = 2.5                 # float
# name = 'Awanish'        # string
# is_cool = True          # bool

# Multiple assignment

x, y, name, is_cool = (1, 2.5, 'Awanish', True)

print (x, y, name, is_cool)

# Basic Maths

a = x + y

# Variable Casting
x = str(x)
y = int(y)
z = float(y)


# Check Variable types

print(type(y))
print(z)
