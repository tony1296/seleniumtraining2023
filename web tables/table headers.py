from selenium import webdriver
from selenium.webdriver.common.by import By
#printing table headers
driver = webdriver.Chrome()
driver.get("file:///C:/Users/HP/Documents/big%20table.html")
driver.maximize_window()
print("Table of headers")
list_elements_headers = driver.find_elements(By.XPATH,"/html/body/table/tbody/tr[1]/th")
for element in list_elements_headers:
    print(element.text)