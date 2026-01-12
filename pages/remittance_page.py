import time

from selenium.webdriver.common.by import By
from Utilities.configReader import readconfig
from Utilities.logger import get_logger
from base.baseClass import BaseUtils

logger = get_logger(__name__)

class Remittance(BaseUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    recipient_country = (By.XPATH, readconfig("Remittance_page", "recipients_country"))
    remittance_page_identifier = (By.XPATH, "//h2[normalize-space()='PAPSS']")
    account_enquiry_name = (By.XPATH, readconfig("Remittance_page", "account_enquiry_name"))
    searchcountry = (By.XPATH, readconfig("Remittance_page", "searchcountry"))
    recipient_bank = (By.XPATH, readconfig("Remittance_page", "recipients_bank"))
    searchbank = (By.XPATH, readconfig("Remittance_page", "searchbank"))
    recipientsaccountNumber = (By.XPATH, readconfig("Remittance_page", "recipients_accountNumber"))
    senderamount = (By.XPATH, readconfig("Remittance_page", "sender_amount"))
    recipientsamount = (By.XPATH, readconfig("Remittance_page", "recipients_amount"))
    narration_box = (By.XPATH, readconfig("Remittance_page", "narration"))
    proceedbutton = (By.XPATH, readconfig("Remittance_page", "proceedbutton"))
    error_text = (By.XPATH, readconfig("Remittance_page", "error_text"))
    principal_amount= (By.XPATH, "//div[@class='flex flex-col gap-[10px]']/div[1]/p[2]")
    amount_fees = (By.XPATH, "//div[@class='flex flex-col gap-[10px]']/div[2]/p[2]")
    vat = (By.XPATH, "//div[@class='flex flex-col gap-[10px]']/div[3]/p[2]")
    total_amount =(By.XPATH, "//div[@class='flex flex-col gap-[10px]']/div[4]/p[2]")
    tokenpageamount = (By.XPATH, "//div[@class='flex flex-col w-full rounded-[15px] py-5 px-8']/div[1]/h1")
    tokenbox = (By.XPATH, "//input[@id='token-input-0']")
    maketransferbutton = (By.XPATH, "//button[normalize-space()='Make Transfer']")
    invalid_token_error = (By.XPATH, "//*[contains(text(),'Invalid Token')]")
    CHARGES_ERROR_SELECTOR = (By.XPATH, readconfig("Remittance_page", "error_text"))  # The error alert

    def wait_for_conversion_result(self):
        return self.wait_for_result(Remittance.principal_amount, Remittance.CHARGES_ERROR_SELECTOR)
        # # Wait up to 15 seconds for EITHER the amount OR the error to appear
        # wait = WebDriverWait(self.driver, 20)
        # try:
        #     # This waits until one of the two elements is present in the DOM
        #     result = wait.until(
        #         lambda driver: self.driver.find_element(Remittance.principal_amount) or
        #                        self.driver.find_elements(Remittance.CHARGES_ERROR_SELECTOR)
        #     )
        #     # Check which one we found
        #     if self.driver.find_elements(*Remittance.CHARGES_ERROR_SELECTOR):
        #         error_text = self.driver.find_element(*Remittance.CHARGES_ERROR_SELECTOR).text
        #         pytest.fail(f"Conversion failed with error: {error_text}")
        #     else:
        #         print("Conversion successful!")
        #         return True
        #
        # except TimeoutException:
        #     pytest.fail("System timed out waiting for conversion result.")

    def token_page_amount_text(self):
        logger.info(f"getting token page amount")
        return self.get_text_js(Remittance.tokenpageamount)

    def click_make_transfer_button(self):
        logger.info(f"clicking make transfer button")
        self.driver.find_element(*Remittance.maketransferbutton).click()

    def confirm_token_page_amount(self, sender_amount):
        logger.info(f"getting amount displayed on token page confirmation modal")
        token_page_amount = self.token_page_amount_text()
        amount = sender_amount.strip()
        if token_page_amount == amount:
            logger(f"amount displayed on token page is the correct principal amount")
        else:
            logger(f"amount displayed on token page is not the correct principal amount, expected '{amount}', got '{token_page_amount}'")
        return self.get_text_js(Remittance.tokenpageamount)

    def enter_invalid_token_and_click_make_transfer_button(self,invalid_token):
        logger.info(f"inputting invalid token")
        put_token = self.driver.find_element(*Remittance.tokenbox)
        put_token.click()
        put_token.send_Keys(invalid_token)
        self.click_make_transfer_button()
        actual_token_error_message = self.get_text_js(Remittance.invalid_token_error)
        logger.info(f"Actual text is: '{actual_token_error_message}'")
        text_locator = Remittance.invalid_token_error
        expected_token_error_message = "Invalid Token"
        is_match = self.compare_text(text_locator, expected_token_error_message)
        if not is_match:
            logger.error(f"Match failed! Expected: '{expected_token_error_message}', Actual: '{actual_token_error_message}'")
            assert False, f"Expected '{expected_token_error_message}' but got '{actual_token_error_message}'"
        logger.info(f"token error message matched")

    def enter_token(self, token):
        logger.info(f"inputting valid token after invalid token validation")
        # self.driver.find_element(By.XPATH, "//input[@id='token-input-7']").clear()
        # self.driver.find_element(By.XPATH, "//input[@id='token-input-6']").clear()
        # self.driver.find_element(By.XPATH, "//input[@id='token-input-5']").clear()
        # self.driver.find_element(By.XPATH, "//input[@id='token-input-4']").clear()
        # self.driver.find_element(By.XPATH, "//input[@id='token-input-3']").clear()
        # self.driver.find_element(By.XPATH, "//input[@id='token-input-2']").clear()
        # self.driver.find_element(By.XPATH, "//input[@id='token-input-1']").clear()
        # self.driver.find_element(By.XPATH, "//input[@id='token-input-0']").clear()
        put_token = self.driver.find_element(*Remittance.tokenbox)
        put_token.click()
        put_token.send_keys(token)

    def total_amount_text(self):
        logger.info(f"getting total amount")
        return self.get_text_js(Remittance.total_amount)

    def fees_text(self):
        logger.info(f"getting fees amount")
        return self.get_text_js(Remittance.amount_fees)

    def vat_text(self):
        logger.info(f"getting vat amount")
        return self.get_text_js(Remittance.vat)

    def principal_amount_text(self):
        logger.info(f"getting principal amount")
        return self.get_text_js(Remittance.principal_amount)
        # self.driver.find_element(*Remittance.principal_amount).text.strip()

    def compute_total_amount_payable(self):
        logger.info(f"comparing token amount to principal amount")
        amount = self.get_numeric_value(self.principal_amount_text())
        vat = self.get_numeric_value(self.vat_text())
        fee = self.get_numeric_value(self.fees_text())
        total = self.get_numeric_value(self.total_amount_text())
        amount_payable = amount + vat + fee
        if round(amount_payable, 2) == round(total, 2): # Using round() helps avoid floating point precision issues (e.g., 10.000000001)
            logger.info(f"amount payable value is correct")
        else:
            logger.warning(f"amount payable value is incorrect, expected '{amount_payable}', got '{total}'")

    # def compute_total_amount_payable(self):
    #     logger.info(f"computing and comparing total amount")
    #     amount = self.principal_amount()
    #     vat = self.vat()
    #     fee = self.fees()
    #     total = self.total_amount()
    #     amount_payable = amount + vat + fee
    #     if amount_payable == total:
    #         logger(f"total amount payable value is correct")
    #     else:
    #         logger(f"total amount payable value is incorrect, expected '{amount_payable}', got '{total}'")

    def click_recipients_country_dropdown(self):
        logger.info(f"clicking country dropdown")
        self.driver.find_element(*Remittance.recipient_country).click()

    def enter_country_in_search_country_search_box(self, country):
        country_to_search = self.driver.find_element(*Remittance.searchcountry)
        country_to_search.click()
        logger.info(f"typing country name")
        country_to_search.send_keys(country)

    def select_fetched_search_country(self, country):
        self.driver.find_element(By.XPATH, f"//p[contains(normalize-space(), '{country}')]").click()

    def click_recipients_bank_dropdown(self):
        logger.info(f"clicking bank dropdown")
        self.driver.find_element(*Remittance.recipient_bank).click()

    def enter_bank_in_search_bank_search_box(self, bank):
        bank_to_search = self.driver.find_element(*Remittance.searchbank)
        bank_to_search.click()
        logger.info(f"typing bank name")
        bank_to_search.send_keys(bank)

    def select_fetched_search_bank(self, bank):
        self.driver.find_element(By.XPATH, f"//p[contains(normalize-space(),'{bank}')]").click()

    def enter_recipients_account_number(self, account_number):
        recipients_account_number = self.driver.find_element(*Remittance.recipientsaccountNumber)
        recipients_account_number.click()
        recipients_account_number.send_keys(account_number)

    def enter_sender_amount(self, sender_amount):
        sender_amount = self.driver.find_element(*Remittance.senderamount)
        sender_amount.click()
        sender_amount.clear()
        sender_amount.send_keys(sender_amount)
        sender_amount.click()

    def click_recipients_amount(self):
        recipient_amount = self.driver.find_element(*Remittance.recipientsamount)
        recipient_amount.click()
        time.sleep(1)
        self.driver.find_element(*Remittance.narration_box).click()
        time.sleep(1)
        # self.driver.find_element(*Remittance.narration_box).click()
        self.scroll_to_bottom()
        print("scrolling to bottom...")

        # recipient_amount.send_keys(recipients_amount)

    def enter_narration(self, narration):
        self.scroll_to_bottom()
        narrations =self.driver.find_element(*Remittance.narration_box)
        narrations.click()
        narrations.send_keys(narration)
        time.sleep(2)

    def verify_remittance_page_access_message_is_displayed(self):
        if self.is_element_visible(self.remittance_page_identifier):
            print("page identifier is visible.")
        else:
            print("page identifier is not visible.")

    def verify_remittance_proceed_button_disabled(self):
        is_disabled = self.check_element_state(self.proceedbutton, "disabled")
        assert is_disabled, "Login button is not disabled as expected"
        print(f"Is button ready to click? {is_disabled}")
        logger.info("Login button is disabled as expected")

    def click_proceed_button(self):
        self.driver.find_element(*Remittance.proceedbutton).click()

    def verify_account_enquiry_name_is_displayed(self):
        if self.is_element_visible(self.account_enquiry_name):
            logger.info(f"receiver account name is visible.")
        else:
            logger.info(f"account name enquiry has failed, recipients name is not visible.")

    def fill_form_without_country(self, sender_amount):
        self.driver.find_element(*Remittance.senderamount).send_keys(sender_amount)
        actual_text = self.driver.find_element(*Remittance.error_text).text.strip()
        logger.info(f"Actual text is: '{actual_text}'")
        text_locator = Remittance.error_text
        expected_text = "Kindly Select a Country!"
        is_match = self.compare_text(text_locator, expected_text)
        if not is_match:
            logger.error(f"Match failed! Expected: '{expected_text}', Actual: '{actual_text}'")
            assert False, f"Expected '{expected_text}' but got '{actual_text}'"
        logger.info(f"text matched")

    def fill_form_without_bank(self, country, sender_amount):
        self.click_recipients_country_dropdown()
        self.enter_country_in_search_country_search_box(country)
        self.select_fetched_search_country(country)
        self.driver.find_element(*Remittance.senderamount).send_keys(sender_amount)
        actual_text = self.driver.find_element(*Remittance.error_text).text.strip()
        text_locator = Remittance.error_text
        logger.info(f" actual error is: '{actual_text}'")
        expected_text = "Kindly Select a Recipient Bank!"
        is_match = self.compare_text(text_locator, expected_text)
        if not is_match:
            logger.error(f"Match failed! Expected: '{expected_text}', Actual: '{actual_text}'")
            assert False, f"Expected '{expected_text}' but got '{actual_text}'"
        logger.info(f"text matched")

    def verify_account_number_minimum_digits(self, bank, incomplete_account_number):
        self.click_recipients_bank_dropdown()
        self.enter_bank_in_search_bank_search_box(bank)
        self.select_fetched_search_bank(bank)
        self.enter_recipients_account_number(incomplete_account_number)
        self.driver.find_element(*Remittance.senderamount).click()
        actual_text = self.driver.find_element(*Remittance.error_text).text.strip()
        logger.info(f" actual error is: '{actual_text}'")
        text_locator = Remittance.error_text
        expected_text = "Account Number cannot be less than 7-digits"
        is_match = self.compare_text(text_locator, expected_text)
        if not is_match:
            logger.error(f"Match failed! Expected: '{expected_text}', Actual: '{actual_text}'")
            assert False, f"Expected '{expected_text}' but got '{actual_text}'"
        logger.info(f"text matched")
        self.driver.find_element(*Remittance.recipientsaccountNumber).clear()

    def verify_minimum_send_amount(self, account_number, invalid_amount):
        self.enter_recipients_account_number(account_number)
        self.driver.find_element(*Remittance.senderamount).send_keys(invalid_amount)
        self.driver.find_element(*Remittance.recipientsamount).click()
        actual_text = self.driver.find_element(*Remittance.error_text).text.strip()
        logger.info(f" actual error is: '{actual_text}'")
        text_locator = Remittance.error_text
        expected_text = "Amount must be at least 10 NGN"
        is_match = self.compare_text(text_locator, expected_text)
        if not is_match:
            logger.error(f"Match failed! Expected: '{expected_text}', Actual: '{actual_text}'")
            assert False, f"Expected '{expected_text}' but got '{actual_text}'"
        logger.info(f"text matched")

    def fill_form_accurately(self, country, bank, account_number, amount, narration):
        self.driver.refresh()
        self.click_recipients_country_dropdown()
        self.enter_country_in_search_country_search_box(country)
        self.select_fetched_search_country(country)
        self.click_recipients_bank_dropdown()
        self.enter_bank_in_search_bank_search_box(bank)
        self.select_fetched_search_bank(bank)
        self.enter_recipients_account_number(account_number)
        self.driver.find_element(*Remittance.senderamount).send_keys(amount)
        self.verify_account_enquiry_name_is_displayed()
        self.enter_narration(narration)
        self.wait_for_conversion_result()
        BaseUtils.scroll_to_bottom(self)
        self.compute_total_amount_payable()

