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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(15)
driver.maximize_window()

time.sleep(1)
driver.find_element_by_xpath("//a[text()='+']").click()
