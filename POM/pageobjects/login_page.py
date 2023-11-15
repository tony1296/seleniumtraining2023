from selenium.webdriver.common.by import By

class loginpage():

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "Email"
        self.password_textbox_id = "Password"
        self.login_button_xpath = "//button[text()='Log in']"

    def enter_username(self, username):
        self.driver.find_element(By.ID,self.username_textbox_id).clear()
        self.driver.find_element(By.ID,self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID,self.password_textbox_id).clear()
        self.driver.find_element(By.ID,self.password_textbox_id).send_keys(password)

    def click_signin(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()
