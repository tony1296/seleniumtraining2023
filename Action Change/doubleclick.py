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
ele1=driver.find_element(By.ID, 'field1')
ele1.clear()
ele1.send_keys("hii")
ele2=driver.find_element(By.ID, 'field2')
ele2.clear()
button=driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
actions=ActionChains(driver)
actions.double_click(button).perform()
time.sleep(6)
