import XLUtils
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://admin-demo.nopcommerce.com")
path = "C:/Users/HP/Documents/nop_login.xlsx"
rows = XLUtils.getRowCount(path, 'Sheet1')
for r in range(2, rows+1):
    username = XLUtils.readData(path, "Sheet1", r, 1)
    password = XLUtils.readData(path, "Sheet1", r, 2)
    driver.find_element(By.ID,"Email").clear()

    driver.find_element(By.ID,"Email").send_keys(username)

    driver.find_element(By.ID,"Password").clear()

    driver.find_element(By.ID,"Password").send_keys(password)

    #button = driver.find_element(By.XPATH,"//button[text()='Log in']")
    #driver.execute_script("arguments[0].click();", button)
    driver.find_element(By.XPATH,"//button[text()='Log in']").submit()

    if driver.title == 'Dashboard / nopCommerce administration':
        print("test passed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test passed")
        time.sleep(5)
        wait = WebDriverWait(driver, 100)
        element = wait.until(EC.element_to_be_clickable(driver.find_element(By.LINK_TEXT,"Logout")))
        element.click()

    else:
        print("test failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test failed")
        print("credentials are wrong")
        time.sleep(5)

