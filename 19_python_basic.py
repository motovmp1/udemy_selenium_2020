############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 18
#
# Lenovo I5 - New lesson
#
# tuple data type (immutable) (tuples)
#
# Function is a statements that perform a specific task
#############################################################


import time


def use_return_value(a, b):
    sum2 = (a + b)
    return sum2


def addinteger(a, b):
    print(f'Sum : {a+b}')


def greet_me(name):
    print("Good morning!")
    print(f'Hello my friend {name}')
    print("This is new print: " + name)
    return 1


# function return value

result = use_return_value(3, 3)
print(f'This is a result value from use_return: {result}')
print(type(result))

new_result = (result + 2)
print(f'new result is : {new_result}')

# call function first position
addinteger(2, 2)


# call function several times
greet_me("Vinicius")

greet_me("Pedro")

greet_me("Vitor")
