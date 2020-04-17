# selenium have a methodo to execute javascript code in it


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
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(15)
driver.maximize_window()


driver.find_element_by_name("name").send_keys("hello")
# when you type using selenium cannot read label ..only get_attribute
print(driver.find_element_by_name("name").get_attribute("value"))

# this is a javascrip commands that make it start
# in java scrip method you need to use (return) to get back the value
print(driver.execute_script(
    'return document.getElementsByName("name")[0].value'))

# driver.find_element_by_xpath("//a[text()='Shop']").click()
time.sleep(2)
button_shop = driver.find_element_by_xpath("//a[text()='Shop']")
driver.execute_script("arguments[0].click();", button_shop)

time.sleep(3)
# this is javscript check the virgula, selenium cannot scroll
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
