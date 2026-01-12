from selenium.webdriver.common.by import By
from base.baseClass import BaseUtils
from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger(__name__)

class RegisterPage(BaseUtils):

    # Locators
    TERMS_AND_CONDITION_PAGE_IDENTIFIER = (By.XPATH, "//h3[text()='Terms and Conditions']")
    OPEN_TERMS_MODAL = (By.XPATH, "//h5[text()='First Online User Terms and Conditions']")
    OPEN_DATA_PROTECTION_MODAL = (By.XPATH, "//h5[text()='Data Protection Statement']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[text()='Close']")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Continue']")
    FORGOT_QUESTION_LINK = (By.XPATH, "//span[text()='Forgot Question?']")
    TERMS_CHECKBOX = (By.CSS_SELECTOR, "input[id*='First Online App User Terms']")
    DATA_PROTECTION_CHECKBOX = (By.CSS_SELECTOR, "input[id*='Data Protection Statement Terms']")
    ACCOUNT_NUMBER_FIELD = (By.CSS_SELECTOR, "input[placeholder='Enter your FirstBank Account Number']")
    ACCOUNT_NUMBER_PAGE_IDENTIFIER = (By.XPATH, "//h2[text()='Give us your Account Number']")
    ACCOUNT_NUMBER_ERROR_MESSAGE_TEXT = (By.XPATH, "//*[contains(text(),'Unable to validate your account number')]")
    DEBIT_CARD_PAGE_IDENTIFIER = (By.XPATH, "//h2[text()='Enter Debit Card Details']")
    CARD_NUMBER_FIELD = (By.CSS_SELECTOR, "input[placeholder='Enter your Card Number']")
    CARD_PIN_FIELD = (By.CSS_SELECTOR, "input[placeholder='Enter your Card PIN']")
    CARD_ERROR_MESSAGE_TEXT = (By.XPATH, "//*[contains(text(),'Invalid card details provided')]")

    # Actions
    def open_page(self):
        logger.info("Opening base URL and navigating to Register page")
        login_page = LoginPage(self.driver)
        login_page.click_register_link()

    def click_continue_button(self):
        logger.info("Clicking Continue button")
        self.click(self.CONTINUE_BUTTON)

    def click_forgot_question_link(self):
        logger.info("Clicking Forgot Question link")
        self.click(self.FORGOT_QUESTION_LINK)

    def provide_account_number(self, account_number: str):
        logger.info(f"Providing account number: {account_number}")
        self.type(self.ACCOUNT_NUMBER_FIELD, account_number)

    def provide_card_number(self, card_number: str):
        logger.info(f"Entering card number: {card_number}")
        self.type(self.CARD_NUMBER_FIELD, card_number)

    def provide_card_pin(self, pin: str):
        logger.info("Entering card PIN")
        self.type(self.CARD_PIN_FIELD, pin)

    def agree_terms_and_data_protection(self):
        logger.info("Agreeing to Terms and Data Protection")
        self.click(self.OPEN_TERMS_MODAL)
        self.click(self.MODAL_CLOSE_BUTTON)
        self.click(self.OPEN_DATA_PROTECTION_MODAL)
        self.click(self.MODAL_CLOSE_BUTTON)
        self.check_checkbox(self.TERMS_CHECKBOX)
        self.check_checkbox(self.DATA_PROTECTION_CHECKBOX)
        self.click(self.CONTINUE_BUTTON)

    def fill_card_info(self, card_number: str, card_pin: str):
        logger.info("Filling card information")
        self.provide_card_number(card_number)
        self.provide_card_pin(card_pin)
        # self.click(self.CONTINUE_BUTTON)
        # self.verify_card_error_message_displayed()

    # Verifiers
    def verify_terms_message_is_displayed(self):
        visible = self.is_visible(self.TERMS_AND_CONDITION_PAGE_IDENTIFIER)
        assert visible, "Terms and Conditions page not displayed"
        logger.info("Terms and Conditions page displayed")

    def check_form_completeness(self):
        has_attribute = self.is_attribute_present(self.CONTINUE_BUTTON, "disabled")
        assert has_attribute, "Continue button is not disabled as expected"
        logger.info("Continue button is disabled as expected")

    def verify_account_number_page_access_message_is_displayed(self):
        visible = self.is_visible(self.ACCOUNT_NUMBER_PAGE_IDENTIFIER)
        assert visible, "Account Number page not displayed"
        logger.info("Account Number page displayed")

    def verify_debit_card_info_page_access_message_is_displayed(self):
        visible = self.is_visible(self.DEBIT_CARD_PAGE_IDENTIFIER)
        assert visible, "Debit Card Info page not displayed"
        logger.info("Debit Card Info page displayed")

    def verify_account_number_error_message_displayed(self):
        visible = self.is_visible(self.ACCOUNT_NUMBER_ERROR_MESSAGE_TEXT)
        assert visible, "Error message should be displayed for validating account info"
        logger.info("Validating account details error message displayed")

    def verify_card_error_message_displayed(self):
        visible = self.is_visible(self.CARD_ERROR_MESSAGE_TEXT)
        assert visible, "Error message should be displayed for invalid card info"
        logger.info("Invalid card details error message displayed")

    def verify_continue_button_is_displayed(self):
        visible = self.is_visible(self.CONTINUE_BUTTON)
        assert visible, "Continue button should be displayed for passing sake on sauce"
        logger.info("Validating continue button is displayed")


