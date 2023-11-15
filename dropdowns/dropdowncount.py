from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://testautomationpractice.blogspot.com")
driver.maximize_window()
driver.implicitly_wait(2)

list_elements=driver.find_elements(By.TAG_NAME,"select")
l=len(list_elements)
print(l)
vdcount=0
ivdcount=0
for i in (list_elements):
    if(i.is_displayed()):
        vdcount=vdcount+1
    else:
        ivdcount=ivdcount+1

print("visible number of drop-downs:", vdcount)
print("invisible number of dropdowns:", ivdcount)
time.sleep(7)