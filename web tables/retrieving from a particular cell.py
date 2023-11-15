from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///C:/Users/HP/Documents/big%20table.html")
driver.maximize_window()
#To identify a cell, row 3 and column 2
c = driver.find_element(By.XPATH,"//*[@name= 'BookTable']/tbody/tr[3]/td[2]")
#print(len(c))
# to get the text
print(c.text)
driver.close()