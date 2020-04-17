# selenium have a methodo to execute javascript code in it


############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 68
#
# Lenovo I5 - New lesson
#
# selenium test begin - find element ID - NAME XPATH CSS CLAS NAME LINK TEXT
#
#  CCS -s tagname[attribute='valeu'] attribute must be unique
#  chromepath plugin webchrome
#
#############################################################

######################################################################################
# https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions
######################################################################################


from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# chrome options...
# start the browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--window-size=800,500")
chrome_options.add_argument('--start-maximized')

#  This is call the browser, executable file trough selenium test invoke
driver = webdriver.Chrome(
    executable_path="/home/elsys/Documents/geckdriver_chrome/chromedriver", options=chrome_options)

# # This is firefox navigator
# driver = webdriver.Firefox(
#     executable_path="/home/elsys/Documents/geckdriver_firefox/geckodriver")


# get the page
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(15)
# driver.maximize_window()


print(driver.title)
