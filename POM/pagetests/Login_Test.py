from selenium import webdriver
import time
import unittest

from POM.pageobjects import login_page

class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        lp = login_page.loginpage(driver)
        lp.enter_username("admin@yourstore.com")
        lp.enter_password("admin")
        lp.click_signin()

    @classmethod
    def tearDown(cls):
        cls.obj = LoginTests()
        cls.obj.test_login_valid()
        cls.driver.close()