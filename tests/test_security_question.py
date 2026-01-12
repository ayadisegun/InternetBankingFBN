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
# from Utilities.conftest import readconfig, set_data, read_data
from base.baseClass import BaseUtils
from Utilities.test_data import TestData
from allure_commons.types import ParameterMode


# driver = None
@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.fixture(autouse=True)
    def settings(self, setup):
        driver = setup
        self.login_page = LoginPage(driver)
        self.security_question_page = SecurityQuestion(driver)
        self.dashboard_page = Dashboard(driver)
        self.admin = TestData.get_user("admin")
        self.sub_user = TestData.get_user("sub_user")

    @pytest.mark.smoke
    def test_invalid_answer(self):
        self.login_page.enter_username(self.sub_user["username"])
        self.login_page.enter_password(self.sub_user["password"])
        self.login_page.click_login_button()
        self.security_question_page.verify_security_page_access_message_is_displayed()
        self.security_question_page.verify_proceed_button_disabled()
        self.security_question_page.enter_security_answer(self.admin["invalidAnswer"])
        self.security_question_page.click_proceed_button()
        self.security_question_page.compare_error_message()

    @pytest.mark.smoke
    def test_valid_answer(self):
        self.security_question_page.clear_security_answer()
        self.security_question_page.answer_security_question()
        self.security_question_page.click_proceed_button()
        self.dashboard_page.verify_dashboard_page_is_displayed()

