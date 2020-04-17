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


# Username login
time.sleep(2)
driver.find_element_by_id("username").send_keys("Vinicius")


# password login
driver.find_element_by_css_selector("#password").clear()
time.sleep(2)
driver.find_element_by_css_selector("#password").send_keys("1111111")
time.sleep(1)


# link text on;y works when we have a ankor 'a' inside the class - remenber that
driver.find_element_by_link_text("Forgot Your Password?").click()


# link to acces //tagname[text()='xxxxxx']
time.sleep(2)
driver.find_element_by_xpath("//a[text()='Cancel']").click()


# //div[@id='usernamegroup']/label child attribute


# created ccs id using class#id


# close all browser
time.sleep(2)
# driver.close()
print("Finished...")
