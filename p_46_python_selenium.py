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


# check the quantity of checkboxes
time.sleep(2)
check_box = driver.find_elements_by_xpath("//input[@type= 'checkbox']")
print(len(check_box))
count = 0
for field in check_box:
    time.sleep(2)
    field.click()
    assert field.is_selected()
    count += 1
    print(count)
# //input[@type= 'checkbox']
