from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://skptricks.github.io/learncoding/selenium-demo/login%20registration%20page/Register.html")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[name='username'][id='regUsername']") .send_keys("Srikanth")