############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 45
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
driver.get("https://www.makemytrip.com/")
driver.implicitly_wait(15)
driver.maximize_window()


# go to search
time.sleep(1)
driver.find_element_by_id("fromCity").click()
time.sleep(1)
driver.find_element_by_css_selector(
    "input[placeholder='From']").send_keys("del")
time.sleep(2)

# # this is find all elements inside the list
# cities = driver.find_elements_by_css_selector("p[class*='blackText']")
# for index, city in enumerate(cities):
#     time.sleep(0.2)
#     print(index, city.text)

# cities = driver.find_elements_by_css_selector("p[class*='blackText']")
# for city in cities:
#     print(city.text)

time.sleep(1)


cities = driver.find_elements_by_css_selector("p[class*='blackText']")
print(f'How many cities: {len(cities)}')
for city in cities:
    print("Choose delhi now...")
    if city.text == "Delhi, India":
        city.click()
        time.sleep(1)
        break


print("Choose India ....")
driver.find_element_by_xpath("//p[text()='Mumbai, India']").click()

print("closing")
time.sleep(3)
driver.close()
