from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.gmail.com")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input#identifierId").send_keys("Srikanth")