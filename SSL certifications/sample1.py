from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By

desired_capabilities=DesiredCapabilities.CHROME.copy()
desired_capabilities['acceptInsecureCerts'] = True
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://expired.badssl.com")
print(driver.find_element(By.TAG_NAME,'h1').text)