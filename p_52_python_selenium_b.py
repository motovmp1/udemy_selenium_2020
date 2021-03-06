############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 52 _ b
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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# variables

validate_text = "option3"


#  This is call the browser, executable file trough selenium test invoke
driver = webdriver.Chrome(
    executable_path="/home/elsys/Documents/geckdriver_chrome/chromedriver")

# # This is firefox navigator
# driver = webdriver.Firefox(
#     executable_path="/home/elsys/Documents/geckdriver_firefox/geckodriver")


# get the page
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# implicitly must be here :
# driver.implicitly_wait(8)
# Global wait is waiting if appear it jumps by your won
driver.maximize_window()

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(3)

count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3

buttons = driver.find_elements_by_xpath(
    "//div[@class='product-action']/button")

for button in buttons:
    time.sleep(1)
    button.click()


driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

# This is expected wait
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
time.sleep(2)
driver.find_element_by_class_name("promoBtn").click()
time.sleep(4)

# This is the same time
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
code_prome = (driver.find_element_by_css_selector(".promoInfo").text)
print(code_prome)
assert "Code" in code_prome


# close all browser
print("closing...")
driver.close()
