#here contains means *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.gmail.com")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[id*='id']") .send_keys("Srikanth")