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
from pages.limit_management_page import LimitRequestPage
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
class TestLimitManagement:

    @pytest.fixture(scope="class", autouse=True)
    def settings(self, request, setup):
        driver = setup
        LoginHelper.login_as_sub_user(driver)
        request.cls.dashboard_page = Dashboard(driver)
        request.cls.limit_page = LimitRequestPage(driver)
        request.cls.limit = TestData.get_user("user_limit")

    @allure.story("Verify limit management self service")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.Smoke
    @pytest.mark.Regression
    def test_limit_management_functionality(self):
        self.dashboard_page.verify_dashboard_page_is_displayed()
        self.limit_page.click_limit_management_menu()
        self.limit_page.create_limit(self.limit["limitAmount"])
        self.limit_page.enter_token(self.limit["token"])
        self.limit_page.validate_limit_success()
        self.limit_page.click_back_to_home_button()




