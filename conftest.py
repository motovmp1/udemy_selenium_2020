#####################################################################
#
# This is a conftest for all files that use pytest fixture
#
# Vinicius Miranda de Pinho
#
# Version 001
#
# fixture are used as a setup and tear down methods
#
# need to make a file that calls conftes that use for all
#
#######################################################################

# --html=report.html
import pytest_html
import selenium

import pytest
import webbrowser
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


import pytest
# this is allow to run only once in the class
# @pytest.fixture(scope="class")
@pytest.fixture()
def setup():
    print("This is conftest first line will call")
    yield
    print(" This is conftest last line will call")


@pytest.fixture()
def dataload():
    print(" :user profile data is being created")
    # TUPLE that we can use for send data into another page
    driver = "ola"
    print(driver)
    return["Vinicius", "Pinho", "www.rahulshettyacademy.com"]


# this is resoruce from pytest please check words param
@pytest.fixture(params=[("chrome", "vini"), ("firefox", "novo"), ("IE", " vini")])
def crossbrowers(request):
    return request.param
