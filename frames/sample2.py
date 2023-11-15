#case2: If frame name is not available
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://jqueryui.com")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.LINK_TEXT, "Autocomplete").click()
time.sleep(3)
ele = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(ele)
time.sleep(5)
driver.find_element(By.ID, "tags").send_keys("java")
time.sleep(5)
driver.switch_to.default_content()
driver.find_element(By.LINK_TEXT, "Accordion").click()
time.sleep(10)