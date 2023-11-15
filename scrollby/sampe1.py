from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.amazon.in")
driver.maximize_window()
driver.implicitly_wait(3)
# Scroll down
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(3)
# Scroll up
driver.execute_script("window.scrollBy(0, -1000);")
time.sleep(3)
# Scroll Element Into view
element = driver.find_element(By.ID,"twotabsearchtextbox")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(2)
driver.execute_script("window.scrollBy(0, -150);")
# Native Way To Scroll Element Into View
time.sleep(2)
driver.execute_script("window.scrollBy(0, -1000);")
location = element.location_once_scrolled_into_view
print("Location:" + str(location))
driver.execute_script("window.scrollBy(0, -150);")