from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, "//*[@id='userName']")
        self.password_input = (By.XPATH, "//*[@id='password']")
        self.login_button = (By.XPATH, "//*[@id='login']")
        self.username_profile = (By.XPATH, "//*[@id='userName-value']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def GetUserName(self):
        return self.driver.find_element(*self.username_profile).text