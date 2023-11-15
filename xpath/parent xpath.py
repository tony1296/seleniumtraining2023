from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://accounts.lambdatest.com/register")
driver.maximize_window()
driver.implicitly_wait(30)
#identifying locator of password in registration page
ele = driver.find_element(By.XPATH,"//input[@name = 'password']//parent::div")
print(ele.get_attribute("class"))
time.sleep(3)
print(driver.current_url)
driver.close()
