############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 25
#
# Lenovo I5 - New lesson
#
# open and ready file txt in python
#
#
#############################################################


import time

# open file txt
file = open('/home/elsys/Desktop/Teste/udemy_selenium_2020/test.txt')

# Read content files as a index
# print(file.read(5))
'''
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()

print(f'Line one is: {line1}')
print(f'Line two is: {line2}')
print(f'Line two is: {line3}')

'''
'''
line = file.readline()
while line != "":
    # line = line[: -1].splitlines()
    print(line)
    time.sleep(1)
    line = file.readline()

print("Outside the loop txt...")
'''

# this is a lista that we can go inside

for index, line in enumerate(file.readlines()):
    time.sleep(1)
    print(index, "- " + line)


# close file txt
file.close()
