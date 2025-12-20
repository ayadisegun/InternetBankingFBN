import time
from selenium.webdriver.common.by import By
from Utilities.configReader import readconfig
from Utilities.logger import get_logger
from base.baseClass import BaseUtils

logger = get_logger(__name__)

class LoginPage(BaseUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.logger = get_logger

    # , password_field, login_button
    UN_field = (By.XPATH, readconfig("login_page", "userbox"))
    LOGIN_PAGE_IDENTIFIER = (By.XPATH, "//h1[text()='Welcome to FirstOnline']")
    ERROR_MESSAGE_TEXT = (By.XPATH, "//*[contains(text(),'Wrong username or password.')]")
    PW_field = (By.XPATH, readconfig("login_page", "passbox"))
    log_but = (By.XPATH, readconfig("login_page", "login"))
    forgot_password = (By.XPATH, readconfig("login_page", "Forgot_password"))
    register = (By.XPATH, readconfig("login_page", "Register"))


    def goto_url(self):
        return self.driver.get(readconfig("setup", "firstonline_url"))

    def verify_login_page_title(self):
        logger.info(f"Verifying login page title")
        title = self.driver.title
        exp_title = "First Bank Internet Banking1"
        if title == exp_title:
            logger.info("Welcome to FirstOnline")
        else:
            self.get_screenshot("Invalid title page")
            logger.warning(f"invalid title, actual title is '{title}'")
        assert "First Bank" in title
        # self.driver.refresh()
        # return LoginPage

    def enter_username(self, username):
        logger.info(f"Entering username: {username}")
        # self.driver.find_element(*LoginPage.UN_field).clear()
        username_field = self.driver.find_element(*LoginPage.UN_field)
        username_field.click()
        time.sleep(1)
        username_field.clear()
        time.sleep(1)
        username_field.send_keys(username)

    def clear_username(self):
        logger.info(f"Clearing username")
        username_field = self.driver.find_element(*LoginPage.UN_field)
        username_field.clear()
        self.driver.refresh()

    def clear_password(self):
        logger.info(f"Clearing password")
        password_field = self.driver.find_element(*LoginPage.PW_field)
        password_field.click()
        password_field.clear()
        self.driver.refresh()

    def enter_password(self, password):
        logger.info(f"Entering password")
        # self.driver.find_element(*LoginPage.PW_field).clear()
        password_field = self.driver.find_element(*LoginPage.PW_field)
        password_field.click()
        time.sleep(1)
        password_field.clear()
        time.sleep(1)
        password_field.send_keys(password)

    def click_login_button(self):
        logger.info(f"Clicking login button")
        self.driver.find_element(*LoginPage.log_but).click()

    def verify_error_message_displayed(self):
        visible = self.is_visible(LoginPage.ERROR_MESSAGE_TEXT)
        assert visible, "Error message should be displayed for invalid login"
        logger.info("Error message displayed")

    def compare_error_message(self):
        actual_text = self.driver.find_element(*LoginPage.ERROR_MESSAGE_TEXT).text.strip()
        text_locator = LoginPage.ERROR_MESSAGE_TEXT
        expected_text = "Wrong username or password."
        is_match = self.compare_text(text_locator, expected_text)
        if not is_match:
            logger.error(f"Match failed! Expected: '{expected_text}', Actual: '{actual_text}'")
            assert False, f"Expected '{expected_text}' but got '{actual_text}'"
        logger.info(f"text matched")

    def verify_login_button_disabled(self):
        is_disabled = self.check_element_state(self.log_but, "disabled")
        assert is_disabled, "Login button is not disabled as expected"
        print(f"Is button ready to click? {is_disabled}")
        logger.info("Login button is disabled as expected")

    def verify_login_button_enabled(self):
        # 4. Check State (Enabled) - Call this after filling fields
        is_enabled = self.check_element_state(self.log_but, "enabled")
        assert is_enabled, "Login button is not disabled as expected"
        print(f"Is button ready to click? {is_enabled}")
        logger.info("Login button is enabled as expected")

    def verify_login_button_state(self):
        is_active = self.is_element_enabled(self.log_but)
        assert not is_active, "Login button is NOT disabled, but it should be!"
        logger.info("Login button is disabled as expected.")

    def verify_login_page_access_message_is_displayed(self):
        # 1. Check Visibility
        if self.is_element_visible(self.LOGIN_PAGE_IDENTIFIER):
            print("page identifier is visible.")
        else:
            print("page identifier is not visible.")

    def forgot_password_button(self):
        self.driver.find_element(*LoginPage.forgot_password).click()
        from POM.forgot_password_page import ForgotPassword
        forgot_password = ForgotPassword(self.driver)
        return forgot_password

    def register_button(self):
        return self.driver.find_element(*LoginPage.register)

    def login_button(self):
        self.driver.find_element(*LoginPage.log_but).click()  # the * is to de-serialise the shop variable in a python


#1949052.tosin - admin - Password@2
#1949052.testguy - sub user - Password@2


