from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options = chrome_options)

________________
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.google.com/")
______________________
from selenium import webdriver


from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")

option.add_argument("start-maximized")

option.add_argument("--disable-extensions")

option.add_experimental_option("prefs",
{"profile.default_content_setting_values.notifications": 2
 })
