import pytest
import allure
from pages.dashboard_page import Dashboard
from pages.otherbanks_transfer_page import OtherbanksTransferPage
from Utilities.login_helper import LoginHelper
from Utilities.test_data import TestData

@allure.feature("Other Bank Transfer")
class TestOtherBankTransfer:

    @pytest.fixture(scope="class", autouse=True)
    def settings(self, request, setup):
        driver = setup
        LoginHelper.login_as_sub_user(driver)
        request.cls.dashboard = Dashboard(driver)
        request.cls.transfer_page = OtherbanksTransferPage(driver)
        request.cls.transfer = TestData.get_transfer("other_bank")

    @allure.story("Other bank transfer with invalid token")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Smoke
    @pytest.mark.Sanity
    @pytest.mark.Regression
    def test_other_bank_transfer_with_invalid_token(self):
        self.dashboard.verify_dashboard_page_is_displayed()
        self.dashboard.navigate_to_other_bank_account_transfer()
        self.transfer_page.verify_transfer_to_other_bank_account_page_displayed()
        self.transfer_page.fill_transfer_form(self.transfer["account_number"], self.transfer["amount"], self.transfer["invalid_token"])
        self.transfer_page.verify_error_message_displayed()
        print("Other Bank Transfer (Invalid Token) test executed successfully.")

    @allure.story("Successful other bank transfer")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.Smoke
    @pytest.mark.Sanity
    @pytest.mark.Regression
    def test_other_bank_transfer_success(self):
        self.dashboard.verify_dashboard_page_is_displayed()
        self.dashboard.navigate_to_other_bank_account_transfer()
        self.transfer_page.verify_transfer_to_other_bank_account_page_displayed()
        self.transfer_page.fill_transfer_form(self.transfer["account_number"], self.transfer["amount"], self.transfer["token"])
        self.transfer_page.verify_transaction_success()
