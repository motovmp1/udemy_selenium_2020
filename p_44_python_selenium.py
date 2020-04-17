############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 44
#
# Lenovo I5 - New lesson
#
# selenium test begin - find element ID - NAME XPATH CSS CLAS NAME LINK TEXT
#
#  CCS -s tagname[attribute='valeu'] attribute must be unique
#  chromepath plugin webchrome
#
#############################################################

from selenium import webdriver
import time


# This is call the browser, executable file trough selenium test invoke
# driver = webdriver.Chrome(
#     executable_path="/home/elsys/Documents/geckdriver_chrome/chromedriver")

# This is firefox navigator
driver = webdriver.Firefox(
    executable_path="/home/elsys/Documents/geckdriver_firefox/geckodriver")


# get the page
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.implicitly_wait(15)
driver.maximize_window()


# //input[@class='btn btn-success']
time.sleep(2)
driver.find_element_by_xpath("//input[@class='btn btn-success']").click()


# message sucess compare
message_top = (driver.find_element_by_class_name("alert-success").text)
print(message_top)

assert "Success!" in message_top

# close all
time.sleep(2)
print("Closing...")
driver.close()
