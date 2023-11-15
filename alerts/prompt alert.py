from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.implicitly_wait(2)

#click on js prompt button
button=driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[3]/button")
button.click()
time.sleep(2)
#switch to alert
a=driver.switch_to.alert
a.send_keys("selenium")
a.accept()
msg=driver.find_element(By.XPATH,"//*[@id='result']").text
#or "//*[text()='You entered: selenium']"
print(msg)
time.sleep(2)
#clicking on ok button
#a.accept()
#closing the window
driver.close()

