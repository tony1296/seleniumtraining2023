from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys

driver = webdriver.Chrome()
driver.get("http://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select_multiple")
driver.maximize_window()
driver.switch_to.frame("iframeResult")
#Automate multiselect dropdown
element=driver.find_element(By.ID,"cars")
sel=Select(element)
actions = ActionChains(driver)
actions.key_down(keys.Keys.CONTROL).perform()
time.sleep(5)
actions.click(sel.select_by_index(0))
time.sleep(5)
actions.click(sel.select_by_index(3))
time.sleep(5)
actions.key_up(keys.Keys.CONTROL).perform()
time.sleep(5)
#sel.deselect_by_visible_text("Audi")
#sel.deselect_by_index(3)
sel.deselect_by_value("audi")
#sel.deselect_all()
time.sleep(5)
driver.close()