

############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 64
#
# Lenovo I5 - New lesson
#
# selenium test begin - find element ID - NAME XPATH CSS CLAS NAME LINK TEXT
#
#  CCS -s tagname[attribute='valeu'] attribute must be unique
#  chromepath plugin webchrome
#
# action class
#############################################################

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


# variables


#  This is call the browser, executable file trough selenium test invoke
driver = webdriver.Chrome(
    executable_path="/home/elsys/Documents/geckdriver_chrome/chromedriver")

# # This is firefox navigator
# driver = webdriver.Firefox(
#     executable_path="/home/elsys/Documents/geckdriver_firefox/geckodriver")


# get the page
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver#")
# implicitly must be here :
driver.implicitly_wait(10)
# Global wait is waiting if appear it jumps by your won
driver.maximize_window()
time.sleep(2)


# actions chains
actions = ActionChains(driver)

# this is allow to check the context inside the page...(bugs was reported in forum)
actions.context_click(driver.find_element_by_id("double-click")).perform()

time.sleep(5)

actions.double_click(driver.find_element_by_id("double-click")).perform()


# swicht to java alerts...all java one... This is python workaround not selenium

time.sleep(2)
alert_pop = driver.switch_to_alert()

print(alert_pop.text)

assert "You double clicked me!!!, You got to be kidding me" == alert_pop.text
print("Pass in assert test")


# this is press the ok button
time.sleep(3)
alert_pop.accept()

# print the pop up is closed

# Close all
time.sleep(2)
print("Closing now...")
driver.close()
