from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://testautomationpractice.blogspot.com")
driver.maximize_window()
driver.execute_script("window.scrollBy(0, 700);")
time.sleep(3)
driver.implicitly_wait(10)
element = driver.find_element(By.ID,"country")

sel = Select(element)
sel.select_by_visible_text("Germany")
sel.select_by_index(1)

sel.first_selected_option.text
print(sel.first_selected_option.text)

#fetch all selected options
list_options=sel.options
print(sel.options)
for op in sel.options:
    print(op.text)