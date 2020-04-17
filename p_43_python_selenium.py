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
driver.get("https://login.salesforce.com")
driver.implicitly_wait(15)
driver.maximize_window()


# print label webpage

label_password = (driver.find_element_by_css_selector(
    "form[name='login'] label:nth-child(3)").text)
print(label_password)
time.sleep(1)
assert "Password" in label_password


label_xpath = (driver.find_element_by_xpath(
    "//label[contains(text(),'Password')]").text)
print(f'this second xpath: {label_xpath}')
