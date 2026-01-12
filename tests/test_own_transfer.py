import pytest
import allure
from pages.dashboard_page import Dashboard
from pages.own_account_transfer_page import OwnAccountTransferPage
from utils.login_helper import LoginHelper

@allure.feature("Own Account Transfer")
class TestOwnAccountTransfer:

    @pytest.fixture(autouse=True)
    def settings(self, driver):
        LoginHelper.login_as_sub_user(driver)
        self.dashboard = Dashboard(driver)
        self.transfer = OwnAccountTransferPage(driver)

    @allure.story("Own account transfer with invalid token")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Sanity
    @pytest.mark.Regression
    @pytest.mark.Smoke
    def test_own_account_transfer_with_invalid_token(self):
        self.dashboard.verify_user_dashboard_page_access_message_is_displayed()
        self.dashboard.navigate_to_own_account_transfer()
        self.transfer.verify_transfer_to_own_account_page_displayed()
        self.transfer.fill_transfer_form(
            amount=500,
            narration="Test Transfer",
            token="12345678"
        )
        self.transfer.verify_error_message_displayed()

    @allure.story("Successful own account transfer")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.Sanity
    @pytest.mark.Regression
    @pytest.mark.Smoke
    def test_own_account_transfer_success(self):
        self.dashboard.verify_user_dashboard_page_access_message_is_displayed()
        self.dashboard.navigate_to_own_account_transfer()
        self.transfer.verify_transfer_to_own_account_page_displayed()
        self.transfer.fill_transfer_form(
            amount=500,
            narration="Test Transfer",
            token="00000000"
        )
        self.transfer.verify_transaction_success()
        self.dashboard.navigate_to_own_account_transfer()
