############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 38
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
driver = webdriver.Chrome(
    executable_path="/home/elsys/Documents/geckdriver_chrome/chromedriver")


# get the page
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.implicitly_wait(15)
driver.maximize_window()


# send to submit button
time.sleep(2)
driver.find_element_by_xpath("//input[@class='btn btn-success']").click()

# time.sleep(2)
# element = (driver.find_element_by_class_name("alert-success").text)
# print(element)

# title name submit sucess
time.sleep(2)
element = (driver.find_element_by_class_name("alert-success").text)
print(element)

assert "Success! The Form has been submitted successfully!." in element

# close all browser
time.sleep(2)
driver.close()
print("Finished...")
