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
# while loop in python
#############################################################
import time

# it = 4
# level = 4

# while (it > 1) or (level > 1):
#     print(it)
#     print("")
#     time.sleep(1)
#     it = it - 1
#     level = level - 2

# print("I am outside the loop")


# while i <= 5:
#     time.sleep(1)
#     print(i)
#     if i == 3:
#         print("If statement was activeted")
#         break
#     i = i + 1
#     print(f'Counter is now : {i}')

# print("If was never done")


# it1 = 4

# while it1 > 1:
#     if it1 != 3:
#         time.sleep(1)
#         print(it1)
#     it1 = it1 - 1

# print("while loop is done")

'''
it = 10

while it > 1:
    if it == 3:
        time.sleep(1)
        break
    print(f'First loop: {it}')
    it = it - 1
    time.sleep(1)
    print(f'Count it loop: {it}')
print("")
print("while loop finished...")

'''


it = 10

while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)

    it = it - 1
print("")
print("Ending loop now...")
