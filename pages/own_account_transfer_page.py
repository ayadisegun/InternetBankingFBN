from selenium.webdriver.common.by import By
from base.baseClass import BaseUtils
from utils.logger import get_logger
import random

logger = get_logger(__name__)

class OwnAccountTransferPage(BaseUtils):

    # Locators
    TRANSFER_TO_OWN_ACCOUNT_HEADER = (By.XPATH, "//h2[contains(text(),'Transfer to Own Account')]")
    CURRENT_BALANCE_TEXT = (By.XPATH, "//span[contains(text(),'₦')]")
    SELECT_DESTINATION_ACCOUNT_HEADER = (By.XPATH, "//h2[contains(text(),'Select Destination Account')]")
    DROPDOWN_ITEMS = (By.XPATH, "//div[contains(@class,'absolute')]//div[@role='option' or self::div]")
    AMOUNT_INPUT = (By.XPATH, "//input[@placeholder='How much are you sending?']")
    NARRATION_INPUT = (By.XPATH, "//input[@placeholder='Write a narration here']")
    PROCEED_BUTTON = (By.XPATH, "//button[contains(text(),'Proceed')]")
    FIRST_OTP_BOX = (By.CSS_SELECTOR, "input")
    MAKE_TRANSFER_BUTTON = (By.XPATH, "//button[contains(text(),'Make Transfer')]")
    TRANSFER_SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(),'Transaction Completed')]")
    ERROR_MESSAGE_TEXT = (By.XPATH, "//*[contains(text(),'Invalid Token')]")
    GENERATE_RECEIPT = (By.XPATH, "//button[contains(text(),'Generate Receipt')]")
    CLICK_ANOTHER_TRANSACTION = (By.XPATH, "//button[contains(text(),'Perform Another Transaction')]")
    CLICK_DASHBOARD = (By.XPATH, "//span[contains(text(),'Dashboard')]")

    # Actions
    def get_current_balance(self) -> float:
        balance_text = self.text_of_element(self.CURRENT_BALANCE_TEXT)
        numeric_part = balance_text.replace("₦", "").replace(",", "").strip()
        balance = float(numeric_part)
        logger.info(f"Current balance: ₦{balance}")
        return balance

    def select_random_destination_account(self):
        logger.info("Selecting a random destination account")
        self.click(self.SELECT_DESTINATION_ACCOUNT_HEADER)
        accounts = self.driver.find_elements(*self.DROPDOWN_ITEMS)
        assert len(accounts) > 0, "No destination accounts found in dropdown."
        random.choice(accounts).click()

    def enter_otp(self, otp_code: str):
        logger.info(f"Entering OTP: {otp_code}")
        self.type(self.FIRST_OTP_BOX, otp_code)

    def make_transfer(self):
        logger.info("Clicking Make Transfer button")
        self.click(self.MAKE_TRANSFER_BUTTON)

    def fill_transfer_form(self, amount: float, narration: str, token: str):
        logger.info("Filling Own Account transfer form")
        self.select_random_destination_account()
        self.type(self.AMOUNT_INPUT, str(amount))
        self.type(self.NARRATION_INPUT, narration)
        self.click(self.PROCEED_BUTTON)
        self.enter_otp(token)
        self.make_transfer()

    # Verifiers
    def verify_transfer_to_own_account_page_displayed(self):
        visible = self.is_visible(self.TRANSFER_TO_OWN_ACCOUNT_HEADER)
        assert visible, "'Transfer to Own Account' page not displayed"
        logger.info("'Transfer to Own Account' page displayed")

    def verify_transaction_success(self):
        self.verify_success_message_displayed()
        self.click(self.GENERATE_RECEIPT)
        self.click(self.CLICK_ANOTHER_TRANSACTION)
        self.click(self.CLICK_DASHBOARD)
        logger.info("Transaction verified successfully")

    def verify_new_balance(self, old_balance: float, amount_sent: float):
        new_balance = self.get_current_balance()
        expected_balance = old_balance - amount_sent
        assert round(new_balance) == round(expected_balance), "Balance not updated correctly after transfer."
        logger.info(f"New balance verified successfully: ₦{new_balance}")

    def verify_error_message_displayed(self):
        visible = self.is_visible(self.ERROR_MESSAGE_TEXT)
        assert visible, "Error message should be displayed for invalid token"
        logger.info("Error message displayed for invalid token")

    def verify_success_message_displayed(self):
        visible = self.is_visible(self.TRANSFER_SUCCESS_MESSAGE)
        assert visible, "Transfer was not successful"
        logger.info("Transfer successful message displayed")
