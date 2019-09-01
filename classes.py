# A class is like a blueprint for creating objects. A object has properties and methods(functions)
# associated with it. Almost everything in python is an Object

# Creating class

class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def hasBirthDay(self):
        self.age += 1

# Inheritance

class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance

    # Overriding
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe {self.balance}' 


# Intialize user object

awanish = User('Awanish Pandey', 'awanish@gmail.com', 30)
ravi = User('Ravi Kumar', 'ravi@gmail.com', 29)

ravi.age = 32

awanish.hasBirthDay()

print(awanish.greeting())

# Initilization customer
gopi = Customer('Gopi Nathan', 'gopin@gmail.com', 40)

gopi.setBalance(2000)

print(gopi.greeting())

