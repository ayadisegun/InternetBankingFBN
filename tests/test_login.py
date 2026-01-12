import sys
import time

import pytest
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    WebDriverException,
    ElementNotInteractableException
)
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard
from pages.security_question_page import SecurityQuestion
from base.baseClass import BaseUtils
from Utilities.test_data import TestData
from allure_commons.types import ParameterMode


# driver = None
# @pytest.mark.sanity
# @pytest.mark.regression
# @pytest.mark.smoke
@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.fixture(autouse=True)
    def pages(self, setup):
        driver = setup
        self.login_page = LoginPage(driver)
        self.security_question_page = SecurityQuestion(driver)
        self.dashboard_page = Dashboard(driver)
        self.admin = TestData.get_user("admin")
        self.sub_user = TestData.get_user("sub_user")

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_login_without_username(self):
        # driver = setup
        # self.driver = driver
        # log = get_logger
        # utils = BaseUtils(self.driver)
        # set_data((readconfig("data", "file")), (readconfig("data", "sheet_name")), 1, 14, "Firstonline_title")
        # set_data((readconfig("data", "file")), (readconfig("data", "sheet_name")), 2, 14, title)
        self.login_page.verify_login_page_title()
        self.login_page.verify_login_page_access_message_is_displayed()
        self.login_page.clear_username()
        self.login_page.enter_password(self.admin["password"])
        self.login_page.verify_login_button_disabled()

    @pytest.mark.smoke
    def test_login_without_password(self):
        self.login_page.clear_password()
        self.login_page.enter_username(self.admin["username"])
        self.login_page.verify_login_button_disabled()

    @pytest.mark.smoke
    def test_login_with_invalid_credentials(self):
        self.login_page.clear_password()
        self.login_page.enter_username(self.admin["invalidUsername"])
        self.login_page.enter_password(self.admin["password"])
        self.login_page.verify_login_button_enabled()
        self.login_page.click_login_button()
        self.login_page.compare_error_message()

    @pytest.mark.smoke
    def test_valid_admin_login(self):
        self.login_page.clear_password()
        self.login_page.enter_username(self.admin["username"])
        self.login_page.enter_password(self.admin["password"])
        self.login_page.click_login_button()
        self.security_question_page.answer_security_question()
        self.security_question_page.click_proceed_button()
        self.dashboard_page.verify_dashboard_page_is_displayed()
        # self.dashboard_page.click_logout_tab()
        # self.dashboard_page.confirm_logout()

    @pytest.mark.skip()
    @pytest.mark.smoke
    def test_valid_sub_user_login(self):
        self.login_page.clear_password()
        self.login_page.enter_username(self.sub_user["username"])
        self.login_page.enter_password(self.sub_user["password"])
        self.login_page.click_login_button()
        self.security_question_page.answer_security_question()
        self.security_question_page.click_proceed_button()
        self.dashboard_page.verify_dashboard_page_is_displayed()


