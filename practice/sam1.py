from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://testautomationpractice.blogspot.com")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//*[@id='name']").clear()
driver.find_element(By.XPATH,"//*[@id='name']").send_keys("Srikanth")
time.sleep(5)
driver.close()