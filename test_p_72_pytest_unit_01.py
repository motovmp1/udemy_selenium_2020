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


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture_demo(self):
        print("I am inside the setup")

    def test_fixture_demo1(self):
        print("I am inside the setup")

    def test_fixture_demo2(self):
        print("I am inside the setup")

    def test_fixture_demo3(self):
        print("I am inside the setup")

    def test_fixture_demo4(self):
        print("I am inside the setup sophia b")
