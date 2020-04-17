# selenium have a methodo to execute javascript code in it


############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 70
#
# Lenovo I5 - New lesson
#
# File should/must to start with the name test_
#
# pytest -v -s name of the file
#
#
#############################################################


import pytest


@pytest.mark.smoke
# test_ method must be test_
def test_first_programa(setup):
    print("new program...")


def test_second_programa(setup):
    print("new program 2 ...")


def test_third_programa_in_first(setup):
    print("new program 2 ...")
