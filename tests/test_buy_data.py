import pytest
import allure
from pages.dashboard_page import Dashboard
from pages.airtimedata_page import AirtimeData
from Utilities.login_helper import LoginHelper
from Utilities.test_data import TestData

@allure.feature("Buy Data ")
class TestBuyData:

    @pytest.fixture(scope="class", autouse=True)
    def settings(self, request, setup):
        driver = setup
        LoginHelper.login_as_sub_user(driver)
        request.cls.dashboard = Dashboard(driver)
        request.cls.airtime_and_data = AirtimeData(driver)
        request.cls.data = TestData.get_airtime_data("data")

    @allure.story("Buy data with invalid token")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Smoke
    @pytest.mark.Sanity
    @pytest.mark.Regression
    def test_buy_data_with_invalid_token(self):
        self.dashboard.verify_dashboard_page_is_displayed()
        self.dashboard.navigate_to_buy_data()
        self.airtime_and_data.verify_buy_data_page_displayed()
        self.airtime_and_data.fill_airtime_form(self.data["phone_number"], self.data["amount"], self.data["invalid_token"])
        self.airtime_and_data.verify_error_message_displayed()
        print("Buy data (Invalid Token) test executed successfully.")

    @allure.story("Successful other bank transfer")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.Smoke
    @pytest.mark.Sanity
    @pytest.mark.Regression
    def test_buy_data_success(self):
        self.dashboard.verify_dashboard_page_is_displayed()
        self.dashboard.navigate_to_buy_data()
        self.airtime_and_data.verify_buy_data_page_displayed()
        self.airtime_and_data.fill_airtime_form(self.data["phone_number"], self.data["amount"], self.data["token"])
        self.airtime_and_data.verify_transaction_success()
