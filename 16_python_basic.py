############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 13
#
# Lenovo I5 - New lesson
#
# tuple data type (immutable) (tuples)
#
# if else flow control Python
#############################################################

obj = [2, 4, 5, 6, 8, 7, 8]

for index, list_obj in enumerate(obj):
    print(index, "->", list_obj)


sumation = 0
for resul in range(1, 6):
    sumation += resul
print(f' This is final result : {sumation}')
assert sumation == 15, "Not match sumation"


for k in range(1, 10, 2):
    print(k, end=" ")


for k1 in range(10):
    print("")
    print(k1, end=" ")
