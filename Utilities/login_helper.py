# from utilities.config import Config
from pages.login_page import LoginPage
from pages.security_question_page import SecurityQuestion
from Utilities.test_data import TestData

class LoginHelper:

    @staticmethod
    def _get_user_by_role(role: str):
        return TestData.get_user(role)

    @staticmethod
    def _perform_login(driver, username: str, password: str):
        login_page = LoginPage(driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()
        security_question_page = SecurityQuestion(driver)
        security_question_page.verify_security_page_access_message_is_displayed()
        security_question_page.answer_security_question()
        security_question_page.click_proceed_button()
        return login_page  # i think it should return dashboard page

    @staticmethod
    def login_as_admin(driver):
        user = LoginHelper._get_user_by_role("admin")
        return LoginHelper._perform_login(driver, user["username"], user["password"])

    @staticmethod
    def login_as_sub_user(driver):
        user = LoginHelper._get_user_by_role("sub_user")
        return LoginHelper._perform_login(driver, user["username"], user["password"])
