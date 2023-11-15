#Navigation commands are used to navigate the page either in forward or backward direction.
#forward() it will forward one page
#back() it will back one page
#refresh() it is refreshing the current page

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://google.com")
driver.find_element(By.NAME,"q").send_keys("selenium")
driver.find_element(By.NAME,"btnK").submit()
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()