from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com")
driver.maximize_window()
#finding the element signup having text as same,here we will locate element using contains through xpath
driver.find_element(By.XPATH,"//a[starts-with(text(), 'Sign')]").click()
time.sleep(3)
print(driver.current_url)
driver.close()