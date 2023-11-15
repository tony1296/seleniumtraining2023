from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.google.co.in")
driver.maximize_window()
driver.implicitly_wait(3)
#driver.execute_script("window.location = 'http://google.com';")
element = driver.find_element(By.NAME,"q")
driver.execute_script("arguments[0].setAttribute('disabled','true');", element)
time.sleep(5)
driver.execute_script("arguments[0].removeAttribute('disabled');", element)
time.sleep(4)