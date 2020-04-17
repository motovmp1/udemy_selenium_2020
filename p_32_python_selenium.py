############################################################
#
# Vinicius Miranda de Pinho
#
# Python3 and Selenium test webdriver
#
# udemy class
#
# basics pythons commands class 32
#
# Lenovo I5 - New lesson
#
# selenium test begin
#
#
#############################################################

from selenium import webdriver
import time


# This is call the browser, executable file trough selenium test invoke
driver = webdriver.Chrome(
    executable_path="/home/elsys/Documents/geckdriver_chrome/chromedriver")


# get the page
driver.get("https://rahulshettyacademy.com/#/index")


driver.implicitly_wait(15)
driver.maximize_window()

# This is call the name page
title_page = driver.title
print(title_page)
assert ("Rahul Shetty Academy" in title_page)
print(f'This is a current page title: --> {driver.current_url}')
time.sleep(2)

# New page
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(f'This is another page: {driver.current_url}')
time.sleep(2)
driver.back()
driver.refresh()
time.sleep(2)


# Close Browser
time.sleep(3)
print("Closing now...")
driver.close()
driver.quit()
