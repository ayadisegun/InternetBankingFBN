import pytest
import allure
from pages.dashboard_page import Dashboard
from pages.airtimedata_page import AirtimeData
from Utilities.login_helper import LoginHelper
from Utilities.test_data import TestData

@allure.feature("Buy Airtime ")
class TestBuyAirtime:

    @pytest.fixture(scope="class", autouse=True)
    def settings(self, request, setup):
        driver = setup
        LoginHelper.login_as_sub_user(driver)
        request.cls.driver = driver
        request.cls.dashboard = Dashboard(driver)
        request.cls.airtime_and_data = AirtimeData(driver)
        request.cls.airtime = TestData.get_airtime_data("airtime")

    @allure.story("Phone number validation for purchase airtime")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Smoke
    @pytest.mark.Sanity
    @pytest.mark.Regression
    def test_invalid_phone_number_message(self):
        self.dashboard.verify_dashboard_page_is_displayed()
        self.dashboard.navigate_to_buy_airtime()
        self.airtime_and_data.verify_buy_airtime_page_displayed()
        self.airtime_and_data.select_network_provider()
        self.airtime_and_data.enter_phone_number_and_onblur(self.airtime["invalid_phone_number"])
        self.airtime_and_data.verify_invalid_phone_number_displayed()


    @allure.story("Over amount limit validation for purchase airtime")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Smoke
    @pytest.mark.Sanity
    @pytest.mark.Regression
    def test_above_recharge_limit_message(self):

        self.dashboard.verify_dashboard_page_is_displayed()
        self.dashboard.navigate_to_buy_airtime()
        self.airtime_and_data.verify_buy_airtime_page_displayed()
        self.airtime_and_data.select_network_provider()
        self.airtime_and_data.enter_phone_number(self.airtime["phone_number"])
        self.airtime_and_data.enter_amount(self.airtime["above_amount"])
        self.driver.refresh()

    @allure.story("Buy airtime with invalid token")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Smoke
    @pytest.mark.Sanity
    @pytest.mark.Regression
    def test_buy_airtime_with_invalid_token(self):
        self.dashboard.verify_dashboard_page_is_displayed()
        self.dashboard.navigate_to_buy_airtime()
        self.airtime_and_data.verify_buy_airtime_page_displayed()
        self.airtime_and_data.fill_airtime_form(self.airtime["phone_number"], self.airtime["amount"], self.airtime["invalid_token"])
        self.airtime_and_data.verify_error_message_displayed()
        print("Buy airtime (Invalid Token) test executed successfully.")


    @allure.story("Successful airtime purchase")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.Smoke
    @pytest.mark.Sanity
    @pytest.mark.Regression
    def test_buy_airtime_success(self):
        self.dashboard.verify_dashboard_page_is_displayed()
        self.dashboard.navigate_to_buy_airtime()
        self.airtime_and_data.verify_buy_airtime_page_displayed()
        self.airtime_and_data.fill_airtime_form(self.airtime["phone_number"], self.airtime["amount"], self.airtime["token"])
        self.airtime_and_data.verify_transaction_success()
