from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://testautomationpractice.blogspot.com")
driver.maximize_window()
driver.implicitly_wait(2)
#click on the "alert" button to generate the simple alert
button = driver.find_element(By.XPATH,"//*[text()='Alert']")
button.click()
#switch the control to the alert window

Alert =driver.switch_to.alert
#Retrieve the message on the Alert window
msg = Alert.text
print("Alert shows following message:"+ msg)
time.sleep(5)
#use the accept() method to accept the alert
Alert.accept()
#Alert.dismiss()
print(" Clicked on the OK button in the Alert Window")
driver.close()