from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://accounts.lambdatest.com/register")
driver.maximize_window()
driver.implicitly_wait(30)
#locate the element with the link blog using following axes
driver.find_element(By.XPATH,"//*[@id='email']//following::input").click()
driver.find_element(By.XPATH,"//*[@id='email']//following::input").send_keys("aaaaa")
print(driver.current_url)
driver.close()