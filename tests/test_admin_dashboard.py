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
from Utilities.login_helper import LoginHelper
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
        LoginHelper.login_as_admin(driver)
        self.dashboard_page = Dashboard(driver)


    @allure.story("Verify admin dashboard visibility")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.Smoke
    @pytest.mark.Regression
    def test_verify_admin_dashboard_is_visible(self):
        self.dashboard_page.verify_dashboard_page_is_displayed()

