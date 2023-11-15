from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://chercher.tech/practice/hidden-division-popup")
driver.find_element(By.XPATH,"//*[text()='View Pop-up']").click()
driver.find_element(By.XPATH,"/html/body/div/div/input").send_keys("Automation")
driver.close()