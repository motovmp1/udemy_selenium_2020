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
# chrome_options.add_argument("--headless")
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

time.sleep(1)
driver.find_element_by_xpath("//a[text()='Shop']").click()

time.sleep(2)
# products = driver.find_elements_by_xpath("//div[@class='card h-100']")

# for product in products:
#     productname = product.find_element_by_xpath("div/h4/a").text
#     if productname == "Blackberry":
#         print(" I am here")
#         product.find_element_by_xpath("div/button").click()


products = driver.find_elements_by_xpath("//div[@class='card h-100']")

for product in products:
    productname = product.find_element_by_xpath("div/h4/a").text
    print(productname)
    if productname == "iphone X":
        print(" I am here")
        product.find_element_by_xpath("div/button").click()

time.sleep(2)
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()

time.sleep(1)

# product_check = driver.find_element_by_xpath(
#     "//a[text()='iphone X']").get_attribute("text")
# print(product_check)

product_check = driver.find_element_by_xpath(
    "//a[text()='iphone X']").text
print(product_check)
assert "iphone X" == product_check
print("assert pass")

driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

time.sleep(4)


# time.sleep(2)
# flag = driver.find_element(By.CSS_SELECTOR, "label:nth-child(2)").click()
# time.sleep(1)

time.sleep(2)
driver.find_element_by_css_selector("label:nth-child(2)").click()


time.sleep(1)
x = (driver.find_element_by_id("checkbox2").is_selected())
print(x)


driver.find_element_by_xpath(
    "//input[@class='btn btn-success btn-lg']").click()


sucess_banner = (driver.find_element_by_xpath(
    "//div[@class='alert alert-success alert-dismissible']").text)

assert "Success!" in sucess_banner
print("assert2 pass")


driver.get_screenshot_as_file("green_message.png")
