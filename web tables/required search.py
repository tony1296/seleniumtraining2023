from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///C:/Users/HP/Documents/big%20table.html")
driver.maximize_window()
# to identify the table rows
r = driver.find_elements(By.XPATH,"//*[@name = 'BookTable']/tbody/tr")
# to identify the table columns
c = driver.find_elements(By.XPATH,"//*[@name = 'BookTable']/tbody/tr[3]/td")
# to get row count with len method
rc = len(r)
# to get column count with len method
cc = len(c)
#to traverse through the table rows and columns excluding headers
for i in range(2, rc + 1):
    for j in range(1, cc + 1):
        d = driver.find_element(By.XPATH,"//tr["+str(i)+"]/td["+str(j)+"]").text
#to search our requires text
m = driver.find_elements(By.XPATH,"//td[text() = 'Mukesh']")
# to get the size of the list with len method
s = len(m)
print(s)
#check if list size is greater than 0
if s > 0:
    print("text found")
driver.close()