from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import screenshots
driver = webdriver.Chrome()
driver.get("http://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
time.sleep(3)
print(driver.title)
assert driver.title == "Dashboard / nopCommerce administration"

driver.get_screenshot_as_png()
driver.save_screenshot("Selenium.png")