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
# dictonary type base in a Key pairs - you choose the key not index
#############################################################


import pprint

# this is tuple
value = (1, 2, 3, "hello", 6, 8)

print(value)


# this is a dictionary

dic = {
    1: 2,
    2: "Ola"


}


pprint.pprint(dic)

print(dic)


# Python3 code to demonstrate working of
# Pretty Print a dictionary with dictionary value
# Using loops

# initializing dictionary
test_dict = {'gfg': {'rate': 5, 'remark': 'good'}, 'cs': {'rate': 3}}

# printing original dictionary  must be cheange into string  (str)
print("The original dictionary is : " + str(test_dict))

# using loops to Pretty Print
print("The Pretty Print dictionary is : ")
for sub in test_dict:
    print(sub)
    for sub_nest in test_dict[sub]:
        print(sub_nest, ':', test_dict[sub][sub_nest])
