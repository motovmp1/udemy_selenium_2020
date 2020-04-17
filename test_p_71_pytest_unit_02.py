# selenium have a methodo to execute javascript code in it


############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 71
#
# Lenovo I5 - New lesson
#
# File should/must to start with the name test_
#
# pytest -v -s name of the file
#
# py.test -v -s run all inside the folder
#
# pytest test_p_70_pytest_unit_01.py -v -s  // only one test
#
# py.test -k third  -v -s this is a key test that you can call
#
# you can mark as a name tag and run using -m that means "mark"
#
# you can skip test using
#
#
# xfail can run but no any alarm
#############################################################


import pytest


# this is marked as smoke
@pytest.mark.smoke
# @pytest.mark.skip
@pytest.mark.xfail
# test_ method must be test_
def test_third_programa(setup):
    print("new program 3...")
    msg = "hello"
    assert "hi" == msg, "This is wrong string compare to system"


# @pytest.fixture()
# def setup():
#     print("I am inside the setup")


def test_fixture_demo(setup):
    print("I am file 71 fixture demo")
