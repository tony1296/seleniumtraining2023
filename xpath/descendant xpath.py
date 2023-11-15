from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://accounts.lambdatest.com/login")
driver.maximize_window()
driver.implicitly_wait(30)
#finding the remember me grandchildren of the login form with field value as remember me
ele=driver.find_element(By.XPATH,"//div[@class='mt-20']//descendant :: a")
print(ele.text)
time.sleep(3)
print(driver.current_url)
driver.close()n