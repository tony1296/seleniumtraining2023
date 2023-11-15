from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")
driver.maximize_window()
driver.implicitly_wait(2)
driver.switch_to.frame("iframeResult")
time.sleep(5)
ele1= driver.find_element(By.XPATH,"//*[@id='vehicle1']")
print("Checkbox is selected? "+ str(ele1.is_selected()))
ele1.click()
print("Checkbox is selected? "+ str(ele1.is_selected()))
time.sleep(2)
ele2= driver.find_element(By.XPATH,"//*[@id='vehicle2']")
print("Checkbox is selected? "+ str(ele2.is_selected()))
ele2.click()
print("Checkbox is selected? "+ str(ele2.is_selected()))
#True if selected , False is not selected
ele3 =driver.find_element(By.XPATH,"//*[@id='vehicle3']")
print("Checkbox is selected? "+ str(ele3.is_selected()))
ele3.click()
print("Checkbox is selected? "+ str(ele3.is_selected()))

