from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://compendiumdev.co.uk/selenium/basic_web_page.html")
driver.maximize_window()
driver.implicitly_wait(30)
ele=driver.find_element(By.XPATH,"//p[@id='para2']//preceding-sibling::p")
print(ele.text)