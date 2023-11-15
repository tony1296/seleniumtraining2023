from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///C:/Users/HP/Documents/big%20table.html")
driver.maximize_window()
l = driver.find_elements(By.XPATH,"//*[@name = 'BookTable']/tbody/tr")
#to get t the row count in len method
print(len(l))
for i in l:
    print(i.text)
driver.quit()