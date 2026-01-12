import pytest
import allure
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from utils.test_data import TestData

@allure.feature("Register")
class TestRegister:

    @pytest.fixture(autouse=True)
    def settings(self, driver):
        self.login_page = LoginPage(driver)
        self.register_page = RegisterPage(driver)
        self.new_user = TestData.get_user("new_user")

    @allure.story("Register with invalid account number")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Sanity
    @pytest.mark.Regression
    def test_register_with_invalid_account_number(self):
        self.register_page.open_page()
        self.register_page.verify_terms_message_is_displayed()
        self.register_page.agree_terms_and_data_protection()
        self.register_page.verify_account_number_page_access_message_is_displayed()
        self.register_page.provide_account_number(self.new_user["accountNumber"])
        self.register_page.click_continue_button()
        self.register_page.verify_account_number_error_message_displayed()

    @allure.story("Register with invalid card")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Sanity
    @pytest.mark.Regression
    def test_register_with_invalid_card(self):
        self.register_page.open_page()
        self.register_page.verify_terms_message_is_displayed()
        self.register_page.agree_terms_and_data_protection()
        self.register_page.verify_account_number_page_access_message_is_displayed()
        self.register_page.provide_account_number(self.new_user["accountNumber"])
        self.register_page.click_continue_button()
        self.register_page.fill_card_info(
            card_number=self.new_user["cardPAN"],
            card_pin=self.new_user["pin"]
        )
        self.register_page.click_continue_button()
        self.register_page.verify_continue_button_is_displayed()
