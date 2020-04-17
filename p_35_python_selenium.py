############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 35
#
# Lenovo I5 - New lesson
#
# selenium test begin - find element ID - NAME XPATH CSS CLAS NAME LINK TEXT
#
#  CCS -s tagname[attribute='value'] attribute must be unique
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

# Type the name inside the field
time.sleep(2)
driver.find_element_by_name("name").send_keys("Vinicius Miranda de Pinho")

# type the email
time.sleep(2)
driver.find_element_by_name("email").send_keys("vinicius.mpinho@gmail.com")

# click in the check box
time.sleep(2)
driver.find_element_by_id("exampleCheck1").click()

# click employed name
time.sleep(2)
driver.find_element_by_xpath("//*[@id='inlineRadio2']").click()


# send to submit button
time.sleep(2)
driver.find_element_by_xpath("//input[@class='btn btn-success']").click()


# close all browser
time.sleep(2)
driver.close()
print("Finished...")
