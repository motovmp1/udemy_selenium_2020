############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 63
#
# Lenovo I5 - New lesson
#
# selenium test begin - find element ID - NAME XPATH CSS CLAS NAME LINK TEXT
#
#  CCS -s tagname[attribute='valeu'] attribute must be unique
#  chromepath plugin webchrome
#
# handle frames
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
driver.get("https://the-internet.herokuapp.com/iframe")
# implicitly must be here :
driver.implicitly_wait(10)
# Global wait is waiting if appear it jumps by your won
driver.maximize_window()
time.sleep(2)


# handle with frames
# iframe ID or name or index
driver.switch_to_frame("mce_0_ifr")
time.sleep(0.2)
driver.find_element_by_id("tinymce").clear()
time.sleep(1)
driver.find_element_by_id("tinymce").send_keys(
    "Vinicius Miranda de Pinho - Master chief...")

# switch to default content
driver.switch_to_default_content()
print(driver.find_element_by_tag_name("h3").text)


title_parent_page = driver.find_element_by_tag_name("h3").text
assert "An iFrame containing the TinyMCE WYSIWYG Editor" == title_parent_page


# close all
time.sleep(2)
print("closing...")
driver.close()
