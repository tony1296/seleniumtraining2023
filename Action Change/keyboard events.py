from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.interaction import KEY
from selenium.webdriver.common import keys

driver=webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
driver.implicitly_wait(2)
search_bar=driver.find_element(By.NAME,"q")
#create the object for action chains
actions = ActionChains(driver)
actions.click(search_bar)
actions.key_down(keys.Keys.SHIFT)
#actions.send_keys ("jfyie")
actions.send_keys("aaaaaaa")

actions.key_up(keys.Keys.SHIFT)
#perform the operation on the element
actions.perform()
time.sleep(7)
