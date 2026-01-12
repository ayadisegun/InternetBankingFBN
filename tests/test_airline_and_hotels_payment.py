import pytest
import allure
from pages.bills_payment_page import BillsPayment
from pages.user_dashboard_page import Dashboard
from Utilities.login_helper import LoginHelper


@allure.feature("Airline and Hotels Payment")
class TestAirlineAndHotels:

    @pytest.fixture(autouse=True)
    def settings(self, setup):
        driver = setup
        LoginHelper.login_as_sub_user(driver)
        self.dashboard = Dashboard(driver)
        self.bills_payment = BillsPayment(driver)

    # Pull the merchant list dynamically
    @pytest.mark.parametrize(
        "merchant",
        BillsPayment.airlines_and_hotel_options
    )
    @allure.story("Airline and Hotels Payment")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Smoke
    @pytest.mark.Sanity
    @pytest.mark.Regression
    def test_airline_and_hotel_payment(self, merchant):
        self.dashboard_page.verify_dashboard_page_is_displayed()
        self.dashboard.navigate_to_buy_airtime()
        self.dashboard.reload_page()
        self.dashboard.wait_for_seconds(5)
        self.dashboard.browser_back()
        self.dashboard.navigate_to_bills_payment()

        # Each merchant becomes its own test case
        with allure.step(f"Processing merchant → {merchant}"):
            self.bills_payment.click(self.bills_payment.AIRLINE_AND_HOTELS)
            self.bills_payment.is_visible(self.bills_payment.AIRLINE_AND_HOTELS_HEADER)

            self.bills_payment.click_option(merchant)
            self.bills_payment.fill_form_and_make_payment(
                customer_id="1234567890",
                amount="2000",
                phone_number="08142939448",
                token="00000000"
            )
