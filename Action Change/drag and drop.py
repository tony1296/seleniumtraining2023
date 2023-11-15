from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(2)
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(3)
source = driver.find_element(By.ID, "draggable")
dest = driver.find_element(By.ID, "droppable")
actions = ActionChains(driver)

actions.click_and_hold(source).move_to_element(dest).release(source).perform()

print(" drag and drop")