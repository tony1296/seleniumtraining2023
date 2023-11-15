from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://testautomationpractice.blogspot.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(3)
element = driver.find_element(By.ID,"country")
sel = Select(element)
sel.select_by_value("germany")
print("Select germany by value")
time.sleep(2)
sel.select_by_index("2")
print("Select value by index 2")
time.sleep(2)
sel.select_by_visible_text("France")
print("select by visible text")
time.sleep(2)
sel.select_by_index(1)
print("select value by index 1")