from selenium.webdriver.common.by import By
from Utilities.configReader import readconfig
from base.baseClass import BaseUtils
from Utilities.logger import get_logger


class BillsPayment(BaseUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    searchbiller = (By.XPATH, readconfig("billers_page", "searchbiller"))
    selectbiller = (By.XPATH, readconfig("billers_page", "selectbiller"))
    searchairline = (By.XPATH, readconfig("billers_page", "searchairline"))
    searchresult = (By.XPATH, readconfig("billers_page", "searchresult"))
    selectpackage = (By.XPATH, readconfig("billers_page", "selectpackage"))
    prepaid = (By.XPATH, readconfig("billers_page", "prepaid"))
    customerid = (By.XPATH, readconfig("billers_page", "customerid"))
    amts = (By.XPATH, readconfig("billers_page", "amount"))
    phonenumber = (By.XPATH, readconfig("billers_page", "phonenumber"))
    proceeds = (By.XPATH, readconfig("billers_page", "proceed"))
    customername = (By.XPATH, readconfig("billers_page", "customername"))
    tokenbox = (By.XPATH, readconfig("billers_page", "token_box"))
    maketransfer = (By.XPATH, readconfig("billers_page", "make_transfer"))
    generatereceipt = (By.XPATH, readconfig("billers_page", "generate_receipt"))
    downloadreceipt = (By.XPATH, readconfig("billers_page", "download_receipt"))
    selectimage = (By.XPATH, readconfig("billers_page", "selectimage"))
    closereceipt = (By.XPATH, readconfig("billers_page", "close_receipt"))


    # Locators
    BILLS_PAYMENT_HEADER = (By.XPATH, "//h2[contains(text(),'Bills Payment')]")
    AIRLINE_AND_HOTELS = (By.XPATH, "//*[contains(text(),'Airlines and Hotel Payments')]")
    AIRLINE_AND_HOTELS_HEADER = (By.XPATH, "//h2[contains(text(),'Airlines and Hotel Payments')]")
    APM_TERMINAL = (By.XPATH, "//*[contains(text(),'APM Terminal')]")
    APM_TERMINAL_HEADER = (By.XPATH, "//h2[contains(text(),'APM Terminal')]")
    CURRENT_BALANCE_TEXT = (By.XPATH, "//p[contains(text(),'Book Balance')]/span")

    # Dynamic locator for each airline/hotel button
    OPTION_BY_TEXT = "//p[contains(text(),'{}')]"

    # Form fields (update these to your real locators)
    PRODUCT_PACKAGE_SELECTION_AAH = (By.XPATH, "//*[contains(text(),'Enter your Product Package')]")
    PRODUCT_POSTPAID = (By.XPATH, "//*[contains(text(),'Postpaid')]")
    CUSTOMER_ID_INPUT = (By.XPATH, "//input[@placeholder='Enter your Customer ID']")
    AMOUNT_INPUT = (By.XPATH, "//input[@placeholder='Enter the Amount']")
    PHONE_NUMBER_INPUT = (By.XPATH, "//input[@placeholder='Enter the Phone Number']")
    PROCEED_BUTTON = (By.XPATH, "//button[contains(text(),'Proceed')]")
    FIRST_OTP_BOX = (By.CSS_SELECTOR, "input")
    MAKE_TRANSFER_BUTTON = (By.XPATH, "//button[contains(text(),'Make Transfer')]")

    airlines_and_hotel_options = [
        "Wakanow",
        "AERO Book-On-Hold",
        "AERO Mobile Book-On-Hold",
        "Arik Air Book-On-Hold",
        "Dana Air- Book On Hold",
        "Hak Air Book-On-Hold",
        "Medview Airlines",
        "South African Airlines",
        "Trips Widget"
    ]

    # Actions
    def get_current_balance(self) -> float:
        balance_t = self.text_of_element(self.CURRENT_BALANCE_TEXT)
        logger.info(f"Raw balance text: {balance_t}")

        numeric_part = balance_t.replace("₦", "").replace(",", "").strip()
        balance = float(numeric_part)

        logger.info(f"Parsed balance: {balance}")
        return balance

    def click_option(self, option_text: str):
        locator = (By.XPATH, self.OPTION_BY_TEXT.format(option_text))
        logger.info(f"Clicking Airline/Hotel Option: {option_text}")
        self.click(locator)

    def access_apm_terminal(self):
        self.click(self.APM_TERMINAL)

    def enter_otp(self, otp_code: str):
        logger.info(f"Entering OTP: {otp_code}")
        self.type(self.FIRST_OTP_BOX, otp_code)

    def click_proceed(self):
        self.click(self.PROCEED_BUTTON)
        logger.info("Clicked Proceed button")

    def make_transfer(self):
        logger.info("Clicking 'Make Transfer' button")
        self.click(self.MAKE_TRANSFER_BUTTON)

    def fill_form_and_make_payment(self, customer_id: str, amount: str, phone_number: str, token: str):
        self.click(self.PRODUCT_PACKAGE_SELECTION_AAH)
        self.click(self.PRODUCT_POSTPAID)
        self.type(self.CUSTOMER_ID_INPUT, customer_id)
        self.type(self.AMOUNT_INPUT, amount)
        self.type(self.PHONE_NUMBER_INPUT, phone_number)
        logger.info("Form filled successfully")
        self.wait_for_seconds(2)
        self.click_proceed()
        self.wait_for_seconds(2)
        self.click_proceed()
        self.enter_otp(token)
        self.make_transfer()

    # Verifiers
    def verify_bills_payment_page_displayed(self):
        visible = self.is_visible(self.BILLS_PAYMENT_HEADER)
        assert visible, "'Bills payment' page not displayed"
        logger.info("'Bills Payment' page displayed")



    def search_biller(self, biller):
        return self.driver.find_element(*BillsPayment.searchbiller).send_keys(biller)

    def select_biller(self):
        return self.driver.find_element(*BillsPayment.selectbiller).click()

    def search_airline(self, airline_name):
        self.driver.find_element(*BillsPayment.searchairline).clear()
        return self.driver.find_element(*BillsPayment.searchairline).send_keys(airline_name)

    def select_search_result(self):
        return self.driver.find_element(*BillsPayment.searchresult).click()

    def select_package(self):
        return self.driver.find_element(*BillsPayment.selectpackage).click()

    def select_prepaid_plan(self):
        return self.driver.find_element(*BillsPayment.prepaid).click()

    def input_customer_id(self, customer_ID):
        return self.driver.find_element(*BillsPayment.customerid).send_keys(customer_ID)

    def enter_amount(self, amount):
        return self.driver.find_element(*BillsPayment.amts).send_keys(amount)

    def enter_phone_number(self, phn_no):
        return self.driver.find_element(*BillsPayment.phonenumber).send_keys(phn_no)

    def proceed(self):
        return self.driver.find_element(*BillsPayment.proceeds).click()

    def get_customername_text(self):
        element = self.driver.find_element(*BillsPayment.customername)
        customername_text = element.text
        return customername_text

    def token_box(self, token):
        return self.driver.find_element(*BillsPayment.tokenbox).send_keys(token)

    def make_transfer(self):
        return self.driver.find_element(*BillsPayment.maketransfer).click()

    def generate_receipt(self):
        return self.driver.find_element(*BillsPayment.generatereceipt).click()

    def download_receipt(self):
        return self.driver.find_element(*BillsPayment.downloadreceipt).click()

    def select_image(self):
        return self.driver.find_element(*BillsPayment.selectimage).click()

    def close_receipt(self):
        self.driver.find_element(*BillsPayment.closereceipt).click()
        from POM.dashboard_page import Dashboard
        dashboard = Dashboard(self.driver)
        return dashboard