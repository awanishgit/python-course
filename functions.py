# A function is a block of code which in only run when it is called. In Python, we do not
# use parantheses and curly brackets, we use indentation with tabs and spaces

#  Create function

def sayHello(name = 'Awanish'):
    '''
    Prints Hello and name
    @param string
    @return string
    '''
    print('Hello '+ name)

# Return Value

def getSum(num1, num2):
    total = num1 + num2
    return total

# print(getSum(3, 5))

# sum = getSum(1, 4)

# print(sum)

def addOneToNum(num):
    num += 1
    return num

num = 5

increamentedNum = addOneToNum(num)

print(increamentedNum)

#  A Lambda function is a small anonymous function.
#  A Lambda function can be take any number of arguments, but can only have one
#  expression. Very similar to JS arrow functions

getSumLamda = lambda num1, num2: num1 + num2

print(getSumLamda(4,6))
