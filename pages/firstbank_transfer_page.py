from selenium.webdriver.common.by import By
from base.baseClass import BaseUtils
from Utilities.logger import get_logger

logger = get_logger(__name__)

class FirstBankTransferPage(BaseUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    TRANSFER_TO_FIRST_BANK_PAGE = (By.XPATH, "//h2[contains(text(),'Transfer to FirstBank Account')]")
    CURRENT_BALANCE_TEXT = (By.XPATH, "//p[contains(text(),'Book Balance')]/span")
    ENTER_ACCOUNT_NUMBER_FIELD = (By.CSS_SELECTOR, "input[placeholder='Enter Account Number']")
    AMOUNT_INPUT = (By.XPATH, "//input[@placeholder='How much are you sending?']")
    NARRATION_INPUT = (By.XPATH, "//input[@placeholder='Write a narration here']")
    PROCEED_BUTTON = (By.XPATH, "//button[contains(text(),'Proceed')]")
    FIRST_OTP_BOX = (By.CSS_SELECTOR, "input")
    MAKE_TRANSFER_BUTTON = (By.XPATH, "//button[contains(text(),'Make Transfer')]")
    ERROR_MESSAGE_TEXT = (By.XPATH, "//*[contains(text(),'Invalid Token')]")
    NARRATION_DROPDOWN = (By.XPATH, "//*[contains(text(),'Select or enter narration')]")
    NARRATION = (By.XPATH, "//*[contains(text(),'Gift')]")
    VIEW_IN_TRANSACTION_REQUESTS_BTN = (By.XPATH, "//button[contains(text(),'View in Transaction Requests')]")

    # Actions
    def get_current_balance(self) -> float:
        balance_text = self.text_of_element(self.CURRENT_BALANCE_TEXT)
        numeric_part = balance_text.replace("₦", "").replace(",", "").strip()
        balance = float(numeric_part)
        logger.info(f"Current balance parsed: ₦{balance}")
        return balance

    def select_narration(self):
        self.click(self.NARRATION_DROPDOWN)
        self.click(self.NARRATION)

    def enter_account_number(self, account_number: str):
        logger.info(f"Entering account number: {account_number}")
        self.type(self.ENTER_ACCOUNT_NUMBER_FIELD, account_number)

    def enter_otp(self, otp_code: str):
        logger.info(f"Entering OTP: {otp_code}")
        self.type(self.FIRST_OTP_BOX, otp_code)

    def make_transfer(self):
        logger.info("Clicking 'Make Transfer' button")
        self.click(self.MAKE_TRANSFER_BUTTON)

    def fill_transfer_form(self, account_number: str, amount: float, token: str):
        logger.info("Filling transfer form")
        self.is_visible(self.ENTER_ACCOUNT_NUMBER_FIELD)
        self.enter_account_number(account_number)
        logger.info(f"Entering amount: ₦{amount}")
        self.type(self.AMOUNT_INPUT, str(amount))
        logger.info(f"selecting narration")
        self.select_narration()
        # self.type(self.NARRATION_INPUT, narration)
        logger.info("Clicking 'Proceed' button")
        self.click(self.PROCEED_BUTTON)
        self.wait_for_seconds(2)
        self.enter_otp(token)
        self.make_transfer()

    # Verifiers
    def verify_transfer_to_first_bank_page_displayed(self):
        self.wait_for_seconds(3)
        logger.info("Verifying 'Transfer to FirstBank Account' page is displayed")
        visible = self.is_visible(self.TRANSFER_TO_FIRST_BANK_PAGE)
        assert visible, "'Transfer to FirstBank Account' page not displayed"
        logger.info("'Transfer to FirstBank Account' page is displayed")


    def verify_transaction_success(self):
        logger.info("Verifying transaction success and navigating to transaction requests")
        self.click(self.VIEW_IN_TRANSACTION_REQUESTS_BTN)

    def verify_new_balance(self, old_balance: float, amount_sent: float):
        new_balance = self.get_current_balance()
        expected_balance = old_balance - amount_sent
        assert round(new_balance) == round(expected_balance), \
            f"Balance not updated correctly after transfer. Expected: {expected_balance}, Got: {new_balance}"
        logger.info(f"New balance verified successfully: ₦{new_balance}")

    def verify_error_message_displayed(self):
        logger.info("Verifying error message is displayed for invalid token")
        assert self.is_visible(self.ERROR_MESSAGE_TEXT), "Error message should be displayed for invalid token"
        self.reload_page()