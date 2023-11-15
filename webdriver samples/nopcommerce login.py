from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.nopcommerce.com/en/login?returnUrl=%2Fen")
driver.find_element(By.ID,"Username").clear()
driver.find_element(By.ID,"Username").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")

driver.find_element(By.XPATH,"/html/body/div[7]/section/div/div/div/div/div/div[2]/div[1]/div[2]/form/div[2]/div[4]/input").click()
