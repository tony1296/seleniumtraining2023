from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from time import sleep
#create the initial window
driver = webdriver.Chrome()
#goto homepage
driver.get("https://the-internet.herokuapp.com/windows")
main_win = driver.current_window_handle
print(main_win)
print(main_win.title)
print(driver.title)
sleep(5)
#click on the link
driver.find_element(By.XPATH,'//*[@id="content"]/div/a').click()
for window in driver.window_handles:
    if window != main_win:
        child_win = window
#change the control to new window page
driver.switch_to.window(child_win)
print(child_win.title())
time.sleep(3)
s = driver.find_element(By.XPATH,"/html/body/div/h3").text
print(s)
driver.close()
driver.quit()