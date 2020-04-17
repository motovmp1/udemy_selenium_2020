############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 26
#
# Lenovo I5 - New lesson
#
# open and ready file txt in python and write TXT
#
#
#############################################################


import time

# this with open and close file fully automatic
'''
# this is allow write inside the list
with open('/home/elsys/Desktop/Teste/udemy_selenium_2020/test.txt', 'r') as reader:
    for line in (reader.readlines()):
        print(line)
'''


# this is allow write inside the list
with open('/home/elsys/Desktop/Teste/udemy_selenium_2020/test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('/home/elsys/Desktop/Teste/udemy_selenium_2020/test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
