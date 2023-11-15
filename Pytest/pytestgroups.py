from selenium import webdriver
import pytest
import warnings

# pytest = [pytest.mark.frontend, pytest.mark.slow]

@pytest.mark.Smoke
def test_reg_valid_data():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")

@pytest.mark.Sanity
def test_login_invalid_data():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")

@pytest.mark.Regression
@pytest.mark.Smoke
def test_invalid_data():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")
#py.test pytestgroups.py -m Smoke -v
#disabling warnings--->pytest--disable-warnings
#pytest -W ignore::pytest.PytestUnknownMarkWarning