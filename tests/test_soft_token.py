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
from pages.dashboard_page import Dashboard
from pages.soft_token_page import SoftTokenPage
from base.baseClass import BaseUtils
from allure_commons.types import ParameterMode
from Utilities.logger import get_logger
from Utilities.login_helper import LoginHelper
from Utilities.test_data import TestData

logger = get_logger(__name__)


# driver = None
# @pytest.mark.sanity
# @pytest.mark.regression
# @pytest.mark.smoke
@allure.feature("Logout")
class TestSoftToken:

    @pytest.fixture(scope="class", autouse=True)
    def settings(self, request, setup):
        driver = setup
        LoginHelper.login_as_admin(driver)
        request.cls.dashboard_page = Dashboard(driver)
        request.cls.soft_token_page = SoftTokenPage(driver)
        request.cls.soft_token = TestData.get_user("soft_token")

    @allure.story("Verify soft token request self service")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.Smoke
    @pytest.mark.Regression
    def test_soft_token_functionality(self):
        self.dashboard_page.verify_dashboard_page_is_displayed()
        self.soft_token_page.click_soft_token_menu()
        self.soft_token_page.search_and_select_users(self.soft_token["users_name"])
        self.soft_token_page.answer_security_question()
        # self.soft_token_page.click_request_enrolment_button()


        # self.soft_token_page.enter_token(self.soft_token["token"])
        # self.soft_token_page.validate_limit_success()
        # self.soft_token_page.click_back_to_home_button()

