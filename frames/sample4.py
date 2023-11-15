from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://retail.onlinesbi.com/retail/login.htm")
driver.maximize_window()
driver.implicitly_wait(2)
#str=driver.page_source
#print(str)
driver.find_element(By.LINK_TEXT,"CONTINUE TO LOGIN").click()
time.sleep(3)
driver.find_element(By.ID,"username").send_keys("asdfggghhh")
driver.find_element(By.NAME,"password").send_keys("kahydd")