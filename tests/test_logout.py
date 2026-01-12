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
from allure_commons.types import ParameterMode
from Utilities.logger import get_logger
from Utilities.login_helper import LoginHelper

logger = get_logger(__name__)


# driver = None
# @pytest.mark.sanity
# @pytest.mark.regression
# @pytest.mark.smoke
@allure.feature("Logout")
class TestLogout:

    @pytest.fixture(scope="class", autouse=True)
    def settings(self, request, setup):
        driver = setup
        LoginHelper.login_as_sub_user(driver)
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = Dashboard(driver)

    @allure.story("Verify logout functionality")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.Smoke
    @pytest.mark.Regression
    def test_verify_logout_functionality(self):
        self.dashboard_page.verify_dashboard_page_is_displayed()
        self.dashboard_page.click_and_confirm_logout()
        self.login_page.verify_login_page_access_message_is_displayed()


