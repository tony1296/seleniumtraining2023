from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://skptricks.github.io/learncoding/selenium-demo/login%20registration%20page/Register.html")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"form input:nth-of-type(1)") .send_keys("Srikanth")
driver.find_element(By.CSS_SELECTOR,"form input:nth-of-type(2)") .send_keys("Srikanth")