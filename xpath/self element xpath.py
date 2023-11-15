from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()
driver.implicitly_wait(30)
#calling self element
ele = driver.find_element(By.XPATH,"//a[contains(text(),'SBI')]/self::a")
print(ele.text)
