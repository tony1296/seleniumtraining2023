from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///C:/Users/HP/Documents/webtable2.html")
driver.maximize_window()
driver.implicitly_wait(2)
ele = driver.find_element(By.XPATH,"/html/body/table/tbody/tr[2]/td[1]").text
print(ele)
driver.quit()