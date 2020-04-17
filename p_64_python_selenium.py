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
driver.get("https://www.familysearch.org/en/")
# implicitly must be here :
driver.implicitly_wait(10)
# Global wait is waiting if appear it jumps by your won
driver.maximize_window()
time.sleep(2)


# action chains

action = ActionChains(driver)

action.move_to_element(driver.find_element_by_xpath(
    "//*[@id='primaryNav']/div[2]/button")).perform()
driver.find_element_by_xpath(
    "//nav[@id='primaryNav']//div[2]").click()
time.sleep(2)

action.move_to_element(driver.find_element_by_link_text(
    "Genealogies")).click().perform()

print("Done")
