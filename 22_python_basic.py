############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 22
#
# Lenovo I5 - New lesson
#
# class and objects in Python child class
#
#
#############################################################


# sum, multi, add, constant

# methods, class, instance, variables

# Self keyword is mandatory calling class


import time

from p_20_python_basic import Calculator


class childimp(Calculator):
    num2 = 200

    def __init__(self):
        print("Now I am inside the second class")
        Calculator.__init__(self, 3, 3, "vini", "pinho")

    def getdataofile(self):
        return (childimp.num2 + self.num)


p3 = childimp()

print(p3.getdataofile())
