from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_radio")
driver.maximize_window()
driver.implicitly_wait(2)
driver.switch_to.frame("iframeResult")
driver.find_element(By.ID,"css").click()