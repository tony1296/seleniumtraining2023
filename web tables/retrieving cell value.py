from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///C:/Users/HP/Documents/big%20table.html")
driver.maximize_window()
driver.implicitly_wait(2)
#identify column values in 3
l = driver.find_elements(By.XPATH,"//*[@name = 'BookTable']/tbody/tr/td[3]")
for i in l:
    print(i.text)
driver.quit()