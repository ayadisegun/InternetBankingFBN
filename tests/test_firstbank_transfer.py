import pytest
import allure
from pages.dashboard_page import Dashboard
from pages.firstbank_transfer_page import FirstBankTransferPage
from Utilities.login_helper import LoginHelper
from Utilities.test_data import TestData

@allure.feature("First Bank Transfer")
class TestFirstBankTransfer:

    @pytest.fixture(scope="class", autouse=True)
    def settings(self, request, setup):
        driver = setup
        LoginHelper.login_as_sub_user(driver)
        request.cls.dashboard_page = Dashboard(driver)
        request.cls.transfer_page = FirstBankTransferPage(driver)
        request.cls.transfer = TestData.get_transfer("first_bank")

    @allure.story("First bank transfer with invalid token")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Smoke
    @pytest.mark.Sanity
    @pytest.mark.Regression
    def test_first_bank_transfer_with_invalid_token(self):
        self.dashboard_page.verify_dashboard_page_is_displayed()
        self.dashboard_page.navigate_to_first_bank_account_transfer()
        self.transfer_page.verify_transfer_to_first_bank_page_displayed()
        self.transfer_page.fill_transfer_form(self.transfer["account_number"], self.transfer["amount"], self.transfer["invalid_token"])
        self.transfer_page.verify_error_message_displayed()

    @allure.story("Successful first bank transfer")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.Smoke
    @pytest.mark.Sanity
    @pytest.mark.Regression
    def test_first_bank_transfer_success(self):
        self.dashboard_page.verify_dashboard_page_is_displayed()
        self.dashboard_page.navigate_to_first_bank_account_transfer()
        self.transfer_page.verify_transfer_to_first_bank_page_displayed()
        self.transfer_page.fill_transfer_form(self.transfer["account_number"], self.transfer["amount"], self.transfer["token"])
        self.transfer_page.verify_transaction_success()
