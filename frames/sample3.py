from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#if the frame is inactive
driver=webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/tinymce")
driver.maximize_window()
driver.implicitly_wait(3)
element = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(element)
e=driver.switch_to.active_element
e.clear()
e.send_keys("AAAAA")
time.sleep(10)