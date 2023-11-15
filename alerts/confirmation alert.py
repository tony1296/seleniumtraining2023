from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
location = "http://www.tizag.com/javascriptT/javascriptalert.php"
driver.get(location)
driver.implicitly_wait(2)

#Click on the "Alert" button to generate the Confirmation Alert
button = driver.find_element(By.XPATH,"/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/div[4]/form/input")
button.click()

#Switch the control to Alert window
obj = driver.switch_to.alert

#Retrieve the message on the alert window
message=obj.text
print("Alert shows following message: "+ message )
time.sleep(2)
obj.accept()
driver.close()