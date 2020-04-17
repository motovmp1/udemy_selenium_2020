############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 57
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
# this is list1 vega
list1 = []

# list2 is list2 vega
list2 = []


# tabela de preco
sec_page_table_price = []

#  This is call the browser, executable file trough selenium test invoke
driver = webdriver.Chrome(
    executable_path="/home/elsys/Documents/geckdriver_chrome/chromedriver")

# # This is firefox navigator
# driver = webdriver.Firefox(
#     executable_path="/home/elsys/Documents/geckdriver_firefox/geckodriver")


# get the page
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# implicitly must be here :
driver.implicitly_wait(10)
# Global wait is waiting if appear it jumps by your won
driver.maximize_window()

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(3)

count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3

buttons = driver.find_elements_by_xpath(
    "//div[@class='product-action']/button")

for button in buttons:
    time.sleep(0.3)
    button.click()

list_vegetables = driver.find_elements_by_xpath("//h4[@class='product-name']")

for list_vege in list_vegetables:
    time.sleep(0.3)
    list1.append(list_vege.text)

print(list1)

time.sleep(0.5)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()


time.sleep(0.5)
list2_vega = driver.find_elements_by_xpath("//p[@class='product-name']")

for lists_vega in list2_vega:
    time.sleep(0.2)
    list2.append(lists_vega.text)

# second list, second page
time.sleep(1)
print(list2)


table_prices = driver.find_elements_by_xpath(
    "//tr/td[5]/p[@class='amount']")

# sum = 0

# for table_price in table_prices:
#     sum = sum + int(table_price.text)

for price_table in table_prices:
    price_table_text = (price_table.text)
    sec_page_table_price.append(price_table_text)

sec_page_table_price = list(map(int, sec_page_table_price))

result_sec_page_price = (sum(sec_page_table_price))


driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
code_prome = (driver.find_element_by_css_selector(".promoInfo").text)
print(code_prome)
assert "Code" in code_prome
time.sleep(2)

assert list1 == list2
print("both list are match")

amount_fob = (driver.find_element_by_xpath("//span[@class='totAmt']").text)
print(type(amount_fob))

amount_fob = int(amount_fob)
print(type(amount_fob))

print(amount_fob)
print(result_sec_page_price)

assert amount_fob == result_sec_page_price
print("sum match")

discount_cupom = (driver.find_element_by_xpath(
    "//span[@class='discountPerc']").text)
print(discount_cupom)

amount_cupom = (driver.find_element_by_xpath(
    "//span[@class='discountAmt']").text)
print(amount_cupom)

amount_cupom_float = float(amount_cupom)

amount_fob_int = int(amount_fob)

assert amount_cupom_float < amount_fob_int
print("compare discount")


# close all browser
print("Closing...")
driver.close()
