from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_radio")
driver.maximize_window()
driver.implicitly_wait(2)
driver.switch_to.frame("iframeResult")

radioButtonsList =driver.find_elements(By.XPATH,"//input[contains(@type,'radio') and contains(@value,'CSS')]")
size = len(radioButtonsList)
print("Size of the list: " + str(size))
for radioButton in radioButtonsList:
 isSelected = radioButton.is_selected()
 if not isSelected:
    radioButton.click()
 time.sleep(2)