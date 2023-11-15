from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://only-testing-blog.blogspot.in/2015/01/iframe1.html")
driver.maximize_window()
driver.implicitly_wait(2)
driver.switch_to.frame("frame1")
driver.find_element(By.XPATH,"//*[@id='post-body-3107268830657760720']/div[1]/table/tbody/tr[2]/td[2]/input").click()
driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("frame2")
driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[1]/form[1]/input[1]").send_keys("aaaaaaaa")
driver.switch_to.default_content()