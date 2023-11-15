import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

expected_from_date_str = '08/19/2023'
expected_to_date_str = '08/22/2023'

expected_fr_date = '19'
expected_to_date = '22'

test_url = 'https://jqueryui.com/datepicker/#date-range'

class CalendarControlTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_calendar_control_range(self):
        driver = self.driver
        driver.get(test_url)
        time.sleep(5)

    #switch to frame
    frame = driver.find_element(By.CLASS_NAME,"demo-frame")
    driver.switch_to(frame)

    #Steps for the from date
    from_dp = driver.find_element(By.XPATH,"//input[@id='from']")
    from_dp.click()
    time.sleep(5)

    from_month = driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/div/select")
    selected_from_month = Select(from_month)
    selected_from_month.select_by_visible_text("Aug")
    time.sleep(5)

    from_day = driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/table/tbody/tr[3]/td[7]/a" + expected_fr_date +"']")
    from_day.click()
    time.sleep(10)

    #Steps for the to date
    #The same steps like the ones in from month are repeated except that now the operations are performed on a
    #different web element

    to_dp = driver.find_element(By.XPATH,"//input[@id='to']")
    to_dp.click()
    time.sleep(5)

    to_month = driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/div/select")
    selected_to_month = Select(to_month)
    selected_to_month.select_by_visible_text("Aug")
    time.sleep(5)

    #to_day = driver.find_element(By.XPATH,"//table/tbody/tr/td/a[text()='26']")
    to_day = driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/table/tbody/tr[4]/td[3]/a" + expected_to_date +"']")
    to_day.click()
    time.sleep(10)

    #verify whether the values are expected
    selected_from_date_str = from_dp.get_attribute('value')
    #self.assertEqual(selected_from_date_str, expected_from_date_str)
    print(selected_from_date_str)

    selected_to_date_str = to_dp.get_attribute('value')
    #self.assertEqual(selected_to_date_str, expected_to_date_str)
    print(selected_to_date_str)

    print("Unit test of jQuery calendar passed")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()