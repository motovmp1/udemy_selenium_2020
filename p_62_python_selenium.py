############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 62
#
# Lenovo I5 - New lesson
#
# selenium test begin - find element ID - NAME XPATH CSS CLAS NAME LINK TEXT
#
#  CCS -s tagname[attribute='valeu'] attribute must be unique
#  chromepath plugin webchrome
#
# Handle new page link.....
#############################################################

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# variables


#  This is call the browser, executable file trough selenium test invoke
driver = webdriver.Chrome(
    executable_path="/home/elsys/Documents/geckdriver_chrome/chromedriver")

# # This is firefox navigator
# driver = webdriver.Firefox(
#     executable_path="/home/elsys/Documents/geckdriver_firefox/geckodriver")


# get the page
driver.get("https://the-internet.herokuapp.com/windows")
# implicitly must be here :
driver.implicitly_wait(10)
# Global wait is waiting if appear it jumps by your won
driver.maximize_window()


# click button
time.sleep(2)
driver.find_element_by_xpath("//a[text()='Click Here']").click()
time.sleep(2)

# index windows when have parent and child pages
childwindow = driver.window_handles[1]
parent_window = driver.window_handles[0]
# swtch window
driver.switch_to_window(childwindow)
print(driver.find_element_by_tag_name("h3").text)
time.sleep(2)
driver.close()
driver.switch_to_window(parent_window)
time.sleep(2)
print(driver.find_element_by_tag_name("h3").text)

assert "Opening a new window" == driver.find_element_by_tag_name("h3").text


# close all windows
print("Closing...")
driver.close()
