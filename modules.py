# A module is basically a file containing a set of function to include in your application.
# There are core python modules, modules you can install using the pip package manager
# (including Django) as well as custom modules

# Core modules

# import datetime
from datetime import date
# import time
from time import time

# Pip module
import camelcase

# Cutom module

# import validator
from validator import validateEmail

today =  date.today()
timestamp = time()

camel = camelcase.CamelCase()
text = 'hello world'
print(camel.hump(text))

email = 'abc@xyz.com'

if validateEmail(email):
    print('Email is valid.')
else:
    print('Email is not valid.')