from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class Testsample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("test completed")

    def test_login(self,test_setup):
        driver.get("https://practice.automationtesting.in/my-account/")
        driver.find_element(By.ID, "username").send_keys("Admin")
        driver.find_element(By.ID, "password").send_keys("admin123")
        driver.find_element(By.NAME, "login").click()

# for reporting
#py.test






