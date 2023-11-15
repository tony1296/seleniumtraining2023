import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class MyTestCase1(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_search(self):
        self.driver.get("http://google.com")
        self.driver.find_element(By.NAME,"q").send_keys("selenium")
        self.driver.find_element(By.NAME,'btnK').submit()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "selenium - Google Search")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main(verbosity=2)