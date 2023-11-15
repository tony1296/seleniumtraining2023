from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://google.com")
driver.find_element(By.NAME,"q").send_keys("automation")
driver.find_element(By.NAME,"btnK").submit()