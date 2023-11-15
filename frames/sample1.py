'''
Frame is a component which it can divide your your webpage in to multiple parts
'''
from selenium import webdriver
import time

#case1: if frame name is available
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://netbanking.hdfcbank.com/netbanking")
driver.maximize_window()
driver.implicitly_wait(2)
driver.switch_to.frame("login_page")
driver.find_element(By.NAME,"fldLoginUserId").send_keys("1000000")