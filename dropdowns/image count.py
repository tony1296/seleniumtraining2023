from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://www.amazon.in")
driver.maximize_window()
list_elements = driver.find_elements(By.XPATH,"(//img)|(//div[@type='image'])")
l = len(list_elements)
print(l)
vdcount=0
ivdcount=0
for i in (list_elements):
    if(i.is_displayed()):
        vdcount=vdcount+1
    else:
        ivdcount=ivdcount+1

print("visible number of images", vdcount)
print("invisible number of images", ivdcount)