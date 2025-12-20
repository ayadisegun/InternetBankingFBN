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
from Utilities.conftest import readconfig, set_data, read_data
from base.baseClass import BaseUtils
from allure_commons.types import ParameterMode


# driver = None
@pytest.mark.usefixtures("setup")
# @pytest.mark.parametrize("sub_user, sub_pass, admn_user, admn_pass, current_password, new_password, "
#                              "service, provider", read_data())

class Test:
    # @pytest.mark.parametrize("sub_user, sub_pass, admn_user, admn_pass, current_password, new_password, "
    #                          "service, provider", read_data()) #not used

    @pytest.fixture(scope="session")
    def context(self):
        return {}

    @allure.title("login")
    @pytest.mark.order(1)
    # def test_login_smoke(self, setup, get_logger,context, sub_user, sub_pass, admn_user, admn_pass, current_password, new_password,
    #                      service, provider):
    def test_login(self, setup, get_logger,context, test_data):

        # allure.dynamic.parameter("sub_user", sub_user, mode=ParameterMode.HIDDEN)
        # allure.dynamic.parameter("admn_user", admn_user, mode=ParameterMode.HIDDEN)
        # allure.dynamic.parameter("sub_pass", sub_pass, mode=ParameterMode.HIDDEN)
        # allure.dynamic.parameter("admn_pass", admn_pass, mode=ParameterMode.HIDDEN)
        # allure.dynamic.parameter("current_password", current_password, mode=ParameterMode.HIDDEN)
        # allure.dynamic.parameter("new_password", new_password, mode=ParameterMode.HIDDEN)
        row = test_data[0]
        admn_user = row["admn_user"]
        admn_pass = row["admn_pass"]
        driver = setup
        self.driver = driver
        log = get_logger
        utils = BaseUtils(self.driver)
        title = self.driver.title
        exp_title = "First Bank Internet Banking"
        if title == exp_title:
            log.info("Welcome to FirstOnline")
        else:
            utils.get_screenshot("wrong_site_admn")
            log.warning("invalid title, actual title is" + title)
        assert "First Bank" in title
        # set_data((readconfig("data", "file")), (readconfig("data", "sheet_name")), 1, 14, "Firstonline_title")
        # set_data((readconfig("data", "file")), (readconfig("data", "sheet_name")), 2, 14, title)
        login_page = LoginPage(self.driver)
        # utils.get_screenshot("login_page")
        login_page.username_field().send_keys(admn_user)
        login_page.password_field().send_keys(admn_pass)
        time.sleep(3)
        security_question_page = login_page.login_button()
        # self.security_question_page = security_question_page
        context["security_question_page"] = security_question_page

    @allure.title("security_question")
    @pytest.mark.order(2)
    def test_security_question(self, get_logger,context):
        security_question_page = context.get("security_question_page")
        if not security_question_page:
            pytest.fail("security_question_page not found in context")
        log = get_logger
        utils = BaseUtils(self.driver)
        QA_MAP = {
            "What is your favourite city?": "lagos",
            "What is your first school name?": "High school",
            "What is your grandfather's occupation?": "farmer",
        }
        security_question = security_question_page.security_question_text().strip()
        answer = QA_MAP.get(security_question)
        if answer:
            log.info(f"Answering security question: '{security_question}'")
            security_question_page.security_answer_box().send_keys(answer)
        else:
            utils.get_screenshot("unknown_security_question")
            log.warning(f"Unknown security question: '{security_question}'")
        dashboard_page = security_question_page.proceed_button()
        # self.dashboard_page = dashboard_page
        context["dashboard_page"] = dashboard_page

    @allure.title("Intrabank Transfer")
    @pytest.mark.order(3)
    def test_intrabank(self, get_logger,context, test_data):
        row = test_data[0]
        account_number = row["account_number"]
        recipient_name = row["recipient_name"]
        amount = row["amount"]
        narration = row["narration"]
        token = row["token"]
        log = get_logger
        utils = BaseUtils(self.driver)
        dashboard_page = context.get("dashboard_page")
        dashboard_page.transfer_tab()
        transfer_page = dashboard_page.first_bank()
        transfer_page.account_number(account_number)
        receivers_name = transfer_page.get_receiver_name_text()
        log.info(receivers_name)
        assert recipient_name in receivers_name
        transfer_page.amount(amount)
        transfer_page.narration(narration)
        utils.scroll_to_bottom()
        transfer_page.proceed_button()
        transfer_page.token_box(token)
        transfer_page.make_transfer()
        transfer_page.generate_receipt()
        time.sleep(6)
        log.info("generating receipt")
        transfer_page.download_receipt()
        time.sleep(6)
        dashboard_page = transfer_page.close_receipt()
        context["dashboard_page"] = dashboard_page

    @allure.title("Bills Payment")
    @pytest.mark.order(4)
    def test_bills_payment(self, get_logger,context,test_data):
        row = test_data[0]
        phone_number = row["phone_number"]
        amount = row["amount"]
        searchbiller_type = row["searchbiller_type"]
        token = row["token"]
        search_airline = row["search_airline"]
        customer_Id = row["customer_Id"]
        billers_name = row["billers_name"]

        log = get_logger
        utils = BaseUtils(self.driver)
        dashboard_page = context.get("dashboard_page")
        billspayment_page = dashboard_page.bills_payment_tab()
        billspayment_page.search_biller(searchbiller_type)
        time.sleep(2)
        billspayment_page.select_biller()
        time.sleep(2)
        billspayment_page.search_airline(search_airline)
        time.sleep(2)
        billspayment_page.select_search_result()
        time.sleep(2)
        billspayment_page.select_package()
        time.sleep(2)
        billspayment_page.select_prepaid_plan()
        billspayment_page.input_customer_id(customer_Id)
        time.sleep(2)
        billspayment_page.enter_amount(amount)
        billspayment_page.enter_phone_number(phone_number)
        utils.scroll_to_bottom()
        billspayment_page.proceed()
        time.sleep(2)
        customer_name = billspayment_page.get_customername_text()
        assert billers_name in customer_name
        billspayment_page.proceed()
        billspayment_page.token_box(token)
        billspayment_page.make_transfer()
        billspayment_page.generate_receipt()
        billspayment_page.download_receipt()
        billspayment_page.select_image()
        time.sleep(6)
        dashboard_page = billspayment_page.close_receipt()
        context["dashboard_page"] = dashboard_page

    @allure.title("Remittance PAPSS")
    @pytest.mark.order(5)
    def test_remittance_papss(self, get_logger,context, test_data):
        row = test_data[0]
        bank = row["bank"]
        amount = row["amount"]
        account_number = row["account_number"]
        country = row["country"]
        narration = row["narration"]

        log = get_logger
        utils = BaseUtils(self.driver)
        dashboard_page = context.get("dashboard_page")
        remittance_page = dashboard_page.remittance_tab()
        remittance_page.recipients_country()
        remittance_page.search_country().send_keys(country)
        remittance_page.select_country(country)
        # self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Ghana')]").click()
        remittance_page.recipients_bank()
        remittance_page.search_bank().send_keys(bank)
        remittance_page.select_bank(bank)
        # self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Bank of Ghana')]").click()
        remittance_page.recipients_accountNumber().send_keys(account_number)
        remittance_page.sender_amount().send_keys(amount)
        remittance_page.narration().send_keys(narration)
        time.sleep(5)
        utils.scroll_to_bottom()
        time.sleep(5)
        dashboard_page = remittance_page.proceed_button()
        dashboard_page.log_out().click()
        time.sleep(2)
        dashboard_page.logout_yes()

