from selenium.webdriver.common.by import By
from Utilities.configReader import readconfig
from base.baseClass import BaseUtils
from Utilities.logger import get_logger

logger = get_logger(__name__)

class AirtimeData(BaseUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    network_provider = (By.XPATH, readconfig("airtimedata_page", "network_provider"))
    airteldata_option = (By.XPATH, readconfig("airtimedata_page", "airteldata_option"))
    mtndata_option = (By.XPATH, readconfig("airtimedata_page", "mtndata_option"))
    glodata_option = (By.XPATH, readconfig("airtimedata_page", "glodata_option"))
    ninemobiledata_option = (By.XPATH, readconfig("airtimedata_page", "9mobiledata_option"))
    phone_number = (By.XPATH, readconfig("airtimedata_page", "input_phone_number"))
    phone_number_validation = (By.XPATH, readconfig("airtimedata_page", "phone_number_validation"))
    data_plan = (By.XPATH, readconfig("airtimedata_page", "data_plan_dropdown"))
    proceed = (By.XPATH, readconfig("airtimedata_page", "proceed_button"))
    token = (By.XPATH, readconfig("airtimedata_page", "token_input"))
    payment = (By.XPATH, readconfig("airtimedata_page", "payment_button"))
    invalid_token = (By.XPATH, readconfig("airtimedata_page", "error_response_invalid_token"))
    Airtel_opt = (By.XPATH, readconfig("airtimedata_page", "Airtel_option"))
    mtn_opt = (By.XPATH, readconfig("airtimedata_page", "mtn_option"))
    glo_opt = (By.XPATH, readconfig("airtimedata_page", "glo_option"))
    ninemobile_opt = (By.XPATH, readconfig("airtimedata_page", "9mobile_option"))
    amounts = (By.XPATH, readconfig("airtimedata_page", "amount"))


    # Locators
    BUY_DATA = (By.XPATH, "//h2[contains(text(),'Buy Data')]")
    BUY_AIRTIME = (By.XPATH, "//h2[contains(text(),'Buy Airtime')]")
    CURRENT_BALANCE_TEXT = (By.XPATH, "//p[contains(text(),'Book Balance')]/span")
    SELECT_NETWORK_PROVIDER = (By.XPATH, "//h2[contains(text(),'Select Network Provider')]")
    SELECT_MTN_TOP_UP = (By.XPATH, "//*[contains(text(),'MTN Topup')]")
    ENTER_PHONE_NUMBER = (By.CSS_SELECTOR, "input[placeholder='Enter the Phone Number']")
    AMOUNT_INPUT = (By.XPATH, "//input[@placeholder='How much are you sending?']")
    PROCEED_BUTTON = (By.XPATH, "//button[contains(text(),'Proceed')]")

    INVALID_PHONE_NUMBER_MESSAGE = (By.XPATH, "//*[contains(text(),'Invalid phone number. Please enter an 11-digit number.')]")
    AMOUNT_ABOVE_LIMIT = (By.XPATH, "//*[contains(text(),'Amount cannot be greater than Limit')]")

    FIRST_OTP_BOX = (By.CSS_SELECTOR, "input")
    MAKE_PAYMENT_BUTTON = (By.XPATH, "//button[contains(text(),'Make Payment')]")
    ERROR_MESSAGE_TEXT = (By.XPATH, "//*[contains(text(),'Invalid Token')]")
    VIEW_IN_TRANSACTION_REQUESTS_BTN = (By.XPATH, "//button[contains(text(),'View in Transaction Requests')]")

    # Actions
    def get_current_balance(self) -> float:
        balance_t = self.text_of_element(self.CURRENT_BALANCE_TEXT)
        logger.info(f"Raw balance text: {balance_t}")
        numeric_part = balance_t.replace("₦", "").replace(",", "").strip()
        balance = float(numeric_part)
        logger.info(f"Parsed balance: {balance}")
        return balance

    def enter_phone_number(self, phone_number: str):
        logger.info(f"Entering account number: {phone_number}")
        self.type(self.ENTER_PHONE_NUMBER, phone_number)

    def enter_phone_number_and_onblur(self, phone_number: str):
        logger.info(f"Entering account number: {phone_number}")
        self.type_and_blur(self.ENTER_PHONE_NUMBER, phone_number)
        logger.info(f"performing onblur input")

    def enter_otp(self, otp_code: str):
        logger.info(f"Entering OTP: {otp_code}")
        self.type(self.FIRST_OTP_BOX, otp_code)

    def select_network_provider(self):
        logger.info("Selecting network provider")
        self.driver.find_element(*AirtimeData.network_provider).click()
        # self.click(self.SELECT_NETWORK_PROVIDER)
        self.driver.find_element(*AirtimeData.mtn_opt).click()
        # self.click(self.SELECT_MTN_TOP_UP)
        self.wait_for_seconds(1)

    def enter_amount(self, amount: str):
        logger.info(f"Entering amount: {amount}")
        self.type(self.AMOUNT_INPUT, amount)

    def make_purchase(self):
        logger.info("Clicking Buy Airtime button")
        self.click(self.MAKE_PAYMENT_BUTTON)

    def fill_airtime_form(self, phone_number: str, amount: float, token: str):
        logger.info("Filling Airtime form")
        self.is_visible(self.ENTER_PHONE_NUMBER)
        self.select_network_provider()
        self.enter_phone_number(phone_number)
        self.type(self.AMOUNT_INPUT, str(amount))
        self.click(self.PROCEED_BUTTON)
        self.enter_otp(token)
        self.make_purchase()

    # Verifiers
    def verify_buy_data_page_displayed(self):
        self.wait_for_seconds(3)
        visible = self.is_visible(self.BUY_DATA)
        assert visible, "'Buy data' page not displayed"
        logger.info("'Buy data' page displayed")

    def verify_buy_airtime_page_displayed(self):
        self.wait_for_seconds(3)
        visible = self.is_visible(self.BUY_AIRTIME)
        assert visible, "'Buy airtime' page not displayed"
        logger.info("'Buy airtime' page displayed")


    def verify_transaction_success(self):
        logger.info("Verifying transaction success")
        self.click(self.VIEW_IN_TRANSACTION_REQUESTS_BTN)
        # Additional transaction verification logic can be added here

    def verify_new_balance(self, old_balance: float, amount_sent: float):
        new_balance = self.get_current_balance()
        expected_balance = old_balance - amount_sent
        assert round(new_balance) == round(expected_balance), "Balance not updated correctly after purchase."
        logger.info(f"New balance verified successfully: ₦{new_balance}")

    def verify_error_message_displayed(self):
        visible = self.is_visible(self.ERROR_MESSAGE_TEXT)
        assert visible, "Error message should be displayed for invalid token"
        logger.info("Error message displayed for invalid token")
        self.reload_page()

    def verify_invalid_phone_number_displayed(self):
        self.wait_for_seconds(2)
        visible = self.is_visible(self.INVALID_PHONE_NUMBER_MESSAGE)
        assert visible, "Error message should be displayed for invalid phone number"
        logger.info("Error message displayed for invalid phone number")
        self.reload_page()

    def verify_above_limit_message_displayed(self):
        visible = self.is_visible(self.AMOUNT_ABOVE_LIMIT)
        assert visible, "Error message should be displayed for amount above limit"
        logger.info("Error message displayed for amount above limit")




    def select_network_provider1(self):
        self.driver.find_element(*AirtimeData.network_provider).click()

    def airteldata(self):
        self.driver.find_element(*AirtimeData.airteldata_option).click()

    def mtndata(self):
        self.driver.find_element(*AirtimeData.mtndata_option).click()

    def glodata(self):
        return self.driver.find_element(*AirtimeData.glodata_option)

    def ninemobiledata(self):
        return self.driver.find_element(*AirtimeData.ninemobiledata_option)

    def input_phone_number(self):
        return self.driver.find_element(*AirtimeData.phone_number)

    def phonenumber_error(self):
        return self.driver.find_element(*AirtimeData.phone_number_validation)

    def data_plan_dropdown(self):
        return self.driver.find_element(*AirtimeData.data_plan)

    def proceed_button(self):
        return self.driver.find_element(*AirtimeData.proceed)

    def airtime_data_token_input(self):
        return self.driver.find_element(*AirtimeData.token)

    def payment_button(self):
        return self.driver.find_element(*AirtimeData.payment)

    def error_invalid_token(self):
        return self.driver.find_element(*AirtimeData.invalid_token)

    def Airtel_option(self):
        return self.driver.find_element(*AirtimeData.Airtel_opt)

    def mtn_option(self):
        return self.driver.find_element(*AirtimeData.mtn_opt)

    def glo_option(self):
        return self.driver.find_element(*AirtimeData.glo_opt)

    def ninemobile_option(self):
        return self.driver.find_element(*AirtimeData.ninemobile_opt)

    def amount(self):
        return self.driver.find_element(*AirtimeData.amounts)

