from selenium.webdriver.common.by import By
from Utilities.configReader import readconfig
from Utilities.logger import get_logger


class ForgotPassword:

    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, readconfig("Forgot_password_page", "username"))
    continue_but = (By.XPATH, readconfig("Forgot_password_page", "continue_button"))
    token = (By.XPATH, readconfig("Forgot_password_page", "token"))

    def enter_username(self):
        return self.driver.find_element(*ForgotPassword.username)

    def continue_button(self):
        return self.driver.find_element(*ForgotPassword.continue_but)

    def enter_token(self):
        return self.driver.find_element(*ForgotPassword.token)

