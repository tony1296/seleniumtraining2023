from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()
driver.implicitly_wait(2)
ele=driver.find_element(By.XPATH,"//*[@id='nav-link-accountList-nav-line-1']")
actions=ActionChains(driver)
actions.move_to_element(ele).perform()
time.sleep(8)
#driver.quit()

