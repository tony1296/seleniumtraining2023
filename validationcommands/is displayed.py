from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_click")
driver.maximize_window()
driver.implicitly_wait(2)
driver.switch_to.frame("iframeResult")
text1 = driver.find_element(By.XPATH,"/html/body/p[1]")
text2 = driver.find_element(By.XPATH, "/html/body/p[2]")
text3 = driver.find_element(By.XPATH, "/html/body/p[3]")
textBoxState = text1.is_displayed()
#true if visible, False if hidden
#Exception if not present in the DOM
print("Text is visible? " + str(textBoxState))
time.sleep(3)
textBoxState = text2.is_displayed()
print("Text is visible? " + str(textBoxState))
time.sleep(3)
textBoxState = text3.is_displayed()
print("Text is visible? " + str(textBoxState))
time.sleep(3)
#click the text
#find the state if the text
text1.click()
textBoxState = text1.is_displayed()
print("Text is visible? " + str(textBoxState))
time.sleep(2)
text2.click()
textBoxState = text2.is_displayed()
print("Text is visible? " + str(textBoxState))
time.sleep(2)
text3.click()
textBoxState = text3.is_displayed()
print("Text is visible? " + str(textBoxState))
time.sleep(2)
