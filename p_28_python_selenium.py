############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 28
#
# Lenovo I5 - New lesson
#
# how to raise exception
#
#
#############################################################


import time

'''
itemcart = 2

if itemcart != 2:
    raise Exception("Produts cart count not match")
else:
    print("pass")


itemcart1 = 2

assert(itemcart1 == 2)
'''

# try , catch

try:
    with open('/home/elsys/Desktop/Teste/udemy_selenium_2020/test.txt', 'r') as reader:
        print("I am here!")
        reader.read()

except Exception as e:
    print(e)
    # print("I wan to catch the fail status here")


# this is will be print no matter what
finally:
    print("This is final print")
