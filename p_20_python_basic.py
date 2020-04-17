############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 20
#
# Lenovo I5 - New lesson
#
# class and objects in Python
#
#
#############################################################


# sum, multi, add, constant

# methods, class, instance, variables

# Self keyword is mandatory calling class


import time


class Calculator:
    # class variable - ony alive if you call ( this is never change or affectec)
    num = 100

    # defaul constructor
    def __init__(self, num1, num2, name1, name2):
        # init will call values imediate no need to call ( this variables change every call obj)
        print("This is first line always works...")
        time.sleep(0.5)
        self.num1 = num1
        self.num2 = num2
        self.result = 0
        self.name1 = name1
        self.name2 = name2

    def getdata(self):
        print("method in class")
        return self.name1, self.name2

    def summation(self):
        time.sleep(0.5)
        # the best way to call variable (num) is using a name class.variable or we can call self.num
        self.result = (self.num1 + self.num2 + Calculator.num)
        return self.result


# instance call
p1 = Calculator(2, 3, "vini", "cibelle")
p2 = Calculator(3, 3, "vini", "cibelle")
print(p1.getdata())
print(p2.getdata())


# variable no need call as function ()
print(p1.num)

# call summation inside the class using p1
print(p1.summation())

# This is a variable for p2 separated
second_process = p2.summation()
print(f'This is a second process: {second_process}')
