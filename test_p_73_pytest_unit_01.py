import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I am last yeld")


@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return["Vinicius", "Pinho", "www.rahulshettyacademy.com"]
