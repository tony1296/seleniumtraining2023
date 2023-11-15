from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://facebook.com")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[id^='em']") .send_keys("Srikanth")