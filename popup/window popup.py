from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#To write the hidden data in window popup
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

#When we are unable to find out the inspect element
#open webpage
#driver.get("protocol://Username:Password@URL_Address");
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
#verify the title
time.sleep(5)
if(driver.title == "The Internet"):
    print("Test Passed");
else:
    print("Test failed");
