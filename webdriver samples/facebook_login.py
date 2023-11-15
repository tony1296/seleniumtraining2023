import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://facebook.com")
driver.find_element(By.ID,"email").send_keys("9700131806")
time.sleep(2)
driver.find_element(By.ID,"pass").send_keys("tony@1296")
time.sleep(2)
driver.find_element(By.NAME,"login").click()