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
from pages.remittance_page import Remittance
from pages.receipt_page import Receipt
from base.baseClass import BaseUtils
from Utilities.test_data import TestData
from Utilities.login_helper import LoginHelper
from allure_commons.types import ParameterMode


# driver = None
# @pytest.mark.sanity
# @pytest.mark.regression
# @pytest.mark.smoke
@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.fixture(autouse=True)
    def settings(self, setup):
        driver = setup
        LoginHelper.login_as_admin(driver)
        self.dashboard_page = Dashboard(driver)
        self.receipt_page = Receipt(driver)
        # self.token_page = Token(driver)
        self.remittance_page = Remittance(driver)
        self.remittance = TestData.get_remittance("remittance")

    @pytest.mark.smoke
    def test_all_form_validations(self):
        self.dashboard_page.verify_dashboard_page_is_displayed()
        self.dashboard_page.click_remittance_tab()
        self.remittance_page.verify_remittance_page_access_message_is_displayed()
        self.remittance_page.fill_form_without_bank(self.remittance["country"], self.remittance["sender_amount"])
        self.remittance_page.verify_account_number_minimum_digits(self.remittance["bank"], self.remittance["incomplete_account_number"])
        self.remittance_page.verify_minimum_send_amount(self.remittance["account_number"], self.remittance["invalid_amount"])
        self.remittance_page.verify_account_enquiry_name_is_displayed()
        self.remittance_page.enter_narration(self.remittance["narration"])

    @pytest.mark.smoke
    def test_user_can_proceed_with_valid_details(self):
        self.remittance_page.fill_form_accurately(self.remittance["country"], self.remittance["bank"], self.remittance["account_number"], self.remittance["sender_amount"], self.remittance["narration"])
        self.remittance_page.compute_total_amount_payable()
        self.remittance_page.click_proceed_button()
        # self.remittance_page.confirm_token_page_amount((self.remittance["sender_amount"]))

    @pytest.mark.smoke
    def test_invalid_token(self):
        self.remittance_page.enter_invalid_token_and_click_make_transfer_button(self.remittance["invalid_token"])

    @pytest.mark.smoke
    def test_valid_token(self):
        self.remittance_page.enter_token(self.remittance["token"])
        self.remittance_page.click_make_transfer_button()

    @pytest.mark.smoke
    def test_receipt(self):
        self.receipt_page.verify_complete_page_is_displayed()
        self.receipt_page.click_generate_receipt_button()
        self.receipt_page.click_download_receipt_button()
        self.receipt_page.click_close_receipt_button()

