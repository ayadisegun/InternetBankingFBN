from selenium.webdriver.common.by import By
from base.baseClass import BaseUtils
from Utilities.logger import get_logger

logger = get_logger(__name__)

class OtherbanksTransferPage(BaseUtils):

    # Locators
    TRANSFER_TO_OTHER_BANKS = (By.XPATH, "//h2[contains(text(),'Transfer to Other Banks')]")
    CURRENT_BALANCE_TEXT = (By.XPATH, "//p[contains(text(),'Book Balance')]/span")
    ENTER_ACCOUNT_NUMBER_FIELD = (By.CSS_SELECTOR, "input[placeholder='Enter Account Number']")
    SEARCH_BANK_NAME = (By.CSS_SELECTOR, "input[placeholder='Search Bank Name']")
    FIND_MORE_BANKS = (By.XPATH, "//*[contains(text(),'Find More Banks')]")
    GT_BANK = (By.XPATH, "//*[contains(text(),'Guaranty Trust Bank')]")
    AMOUNT_INPUT = (By.XPATH, "//input[@placeholder='How much are you sending?']")
    NARRATION_INPUT = (By.XPATH, "//input[@placeholder='Write a narration here']")
    PROCEED_BUTTON = (By.XPATH, "//button[contains(text(),'Proceed')]")
    FIRST_OTP_BOX = (By.CSS_SELECTOR, "input")
    MAKE_TRANSFER_BUTTON = (By.XPATH, "//button[contains(text(),'Make Transfer')]")
    ERROR_MESSAGE_TEXT = (By.XPATH, "//*[contains(text(),'Invalid Token')]")
    VIEW_IN_TRANSACTION_REQUESTS_BTN = (By.XPATH, "//button[contains(text(),'View in Transaction Requests')]")
    NARRATION_DROPDOWN = (By.XPATH, "//*[contains(text(),'Select or enter narration')]")
    NARRATION = (By.XPATH, "//*[contains(text(),'Gift')]")


    # Actions
    def get_current_balance(self) -> float:
        balance_text = self.text_of_element(self.CURRENT_BALANCE_TEXT)
        logger.info(f"Raw balance text: {balance_text}")
        numeric_part = balance_text.replace("₦", "").replace(",", "").strip()
        balance = float(numeric_part)
        logger.info(f"Parsed balance: {balance}")
        return balance

    def select_narration(self):
        self.click(self.NARRATION_DROPDOWN)
        self.click(self.NARRATION)


    def enter_account_number(self, account_number: str):
        logger.info(f"Entering account number: {account_number}")
        self.type(self.ENTER_ACCOUNT_NUMBER_FIELD, account_number)

    def enter_search_term(self, search_param: str):
        logger.info(f"Entering search term: {search_param}")
        self.type(self.SEARCH_BANK_NAME, search_param)

    def find_more_banks(self):
        logger.info("Clicking 'Find More Banks'")
        self.click(self.FIND_MORE_BANKS)

    def select_gt_bank(self):
        logger.info("Selecting GT Bank")
        self.click(self.GT_BANK)

    def enter_otp(self, otp_code: str):
        logger.info(f"Entering OTP: {otp_code}")
        self.type(self.FIRST_OTP_BOX, otp_code)

    def make_transfer(self):
        logger.info("Clicking Make Transfer button")
        self.click(self.MAKE_TRANSFER_BUTTON)

    def fill_transfer_form(self, account_number: str, amount: float, token: str):
        logger.info("Filling transfer form")
        self.is_visible(self.ENTER_ACCOUNT_NUMBER_FIELD)
        self.enter_account_number(account_number)
        self.enter_search_term("gu")
        self.is_visible(self.FIND_MORE_BANKS)
        self.find_more_banks()
        self.is_visible(self.GT_BANK)
        self.select_gt_bank()
        self.type(self.AMOUNT_INPUT, str(amount))
        logger.info(f"selecting narration")
        self.select_narration()
        self.click(self.PROCEED_BUTTON)
        self.enter_otp(token)
        self.make_transfer()

    # Verifiers
    def verify_transfer_to_other_bank_account_page_displayed(self):
        visible = self.is_visible(self.TRANSFER_TO_OTHER_BANKS)
        assert visible, "'Transfer to Other Bank Account' page not displayed"
        logger.info("'Transfer to Other Bank Account' page displayed")

    def verify_transaction_success(self):
        logger.info("Verifying transaction success")
        self.click(self.VIEW_IN_TRANSACTION_REQUESTS_BTN)
        # Additional transaction verification logic can be added here

    def verify_new_balance(self, old_balance: float, amount_sent: float):
        new_balance = self.get_current_balance()
        expected_balance = old_balance - amount_sent
        assert round(new_balance) == round(expected_balance), "Balance not updated correctly after transfer."
        logger.info(f"New balance verified successfully: ₦{new_balance}")

    def verify_error_message_displayed(self):
        visible = self.is_visible(self.ERROR_MESSAGE_TEXT)
        assert visible, "Error message should be displayed for invalid token"
        logger.info("Error message displayed for invalid token")
        self.reload_page()
