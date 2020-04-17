############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 46
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
from selenium.webdriver.common.by import By


# variables

validate_text = "option3"


#  This is call the browser, executable file trough selenium test invoke
driver = webdriver.Chrome(
    executable_path="/home/elsys/Documents/geckdriver_chrome/chromedriver")

# # This is firefox navigator
# driver = webdriver.Firefox(
#     executable_path="/home/elsys/Documents/geckdriver_firefox/geckodriver")


# get the page
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(15)
driver.maximize_window()


# enter name in option box
time.sleep(2)
# driver.find_element_by_css("#name")
driver.find_element_by_id("name").send_keys(validate_text)
time.sleep(2)
driver.find_element_by_id("alertbtn").click()
time.sleep(3)

# swicht to java alerts...all java one... This is python workaround not selenium
alert = driver.switch_to_alert()
print(alert.text)
assert validate_text in alert.text
time.sleep(2)
# alert can use accept, for cancel we have dismiss  alert.dismiss()
alert.accept()

# Close all instance
print("closing....")
time.sleep(2)
driver.close()
