# ACTION chains are used to handle keyboard and mouse events
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://amazon.in")
driver.maximize_window()
driver.implicitly_wait(2)
ele=driver.find_element(By.ID, "twotabsearchtextbox")
actions=ActionChains(driver)
actions.click().perform()
actions.context_click(ele).perform()
time.sleep(5)