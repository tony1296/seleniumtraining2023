from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.google.co.in")
driver.maximize_window()
driver.implicitly_wait(3)

height = driver.execute_script("return window.innerHeight;")
width = driver.execute_script("return window.innerWidth;")
print("Height: " + str(height))
print("Width: " + str(width))
driver.quit()