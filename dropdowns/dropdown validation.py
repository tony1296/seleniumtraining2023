from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://testautomationpractice.blogspot.com")
driver.maximize_window()
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(3)
driver.implicitly_wait(10)

element = driver.find_element(By.ID,"colors")

sel = Select(element)
if(sel.is_multiple):

    print("multi-select")

else:
    print("single-select")

element = driver.find_element(By.ID, "country")

sel = Select(element)
if (sel.is_multiple):

    print("multi-select")

else:
    print("single-select")