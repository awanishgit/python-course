# If/ Else conditions are used to decide to do something based on something being true or false
x = 40
y = 40

# Comparison operators (==, !=, >, <, >=, <=) - Use to compare values

# Simple if
if x == y:
    print(f'{x} is equal to {y}')

# Simple If/ else

if x > y:
    print (f'{x} is greater than {y}')
else:
    print(f'{x} is less than {y}')

# Else If

if x > y:
    print (f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is less than {y}')

# Nested If

if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')

# Logical operator (and, or, not) - Used to combine conditional statement

# and operator

if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# or operator

if x > 2 or x <= 10:
    print(f'{x} is greater than 2 or less than 10')

# not operator

if not x == y:
    print(f'{x} is not equal to {y}')

# Membership Operators (not, not in) - Membership Operators are used to test if a 
# sequence is presented in an object

number = [1, 2, 3, 4, 5]

# in operator

if x in number:
    print(x in number)

if x not in number:
    print(x not in number)

# Identity Operators (is, is not) - Compare the object, not if they are equal, but
# if they are actually the same object, with the same memory location

#  is operator

if x is y:
    print(x is y)

# is not operator

if x is not y:
    print(x is not y)

