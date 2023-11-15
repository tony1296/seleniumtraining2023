from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://testautomationpractice.blogspot.com")
driver.maximize_window()
driver.implicitly_wait(2)

button = driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button[2]")
button.click()
time.sleep(2)

Alert =driver.switch_to.alert
time.sleep(5)
Alert.accept()
driver.close()