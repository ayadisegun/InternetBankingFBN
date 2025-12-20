import time

from selenium.webdriver.common.by import By
from Utilities.configReader import readconfig
from Utilities.logger import get_logger
from base.baseClass import BaseUtils

logger = get_logger(__name__)

class Receipt(BaseUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    transaction_completed = (By.XPATH, "//p[normalize-space()='Transaction Completed']")
    generate_receipt_button = (By.XPATH, "//button[normalize-space()='Generate Receipt']")
    receipt_amount = (By.XPATH, "//p[@class='text-[22px] font-semibold text-[#3E4652] my-2']")
    download = (By.XPATH, "//button[normalize-space()='Download Receipt']")
    share = (By.XPATH, "//button[normalize-space()='Share Receipt']")
    close = (By.XPATH, "//button[contains(@class,'absolute top-4 right-4 rounded-full border-2 p-2')]")

    def verify_complete_page_is_displayed(self):
        actual_text = self.get_text_js(Receipt.transaction_completed)
        expected_text = "Transaction Completed"
        if actual_text == expected_text:
            logger.info(f"completed page is displayed")
        else:
            logger.info(f"completed page is not displayed, expected '{expected_text}', got '{actual_text}'")

    def click_generate_receipt_button(self):
        logger.info(f"clicking generate receipt button")
        self.driver.find_element(*Receipt.generate_receipt_button).click()
        receipt_amount = self.get_text_js(Receipt.receipt_amount)
        if receipt_amount == "":
            logger.info(f"receipt amount is not displayed, receipt not generated")
        else:
            logger.info(f"receipt successfully generated")

    def click_share_receipt_button(self):
        logger.info(f"clicking share receipt button")
        self.driver.find_element(*Receipt.share).click()

    def click_download_receipt_button(self):
        logger.info(f"clicking download receipt button")
        self.driver.find_element(*Receipt.download).click()
        time.sleep(2)

    def click_close_receipt_button(self):
        logger.info(f"clicking close receipt button")
        self.driver.find_element(*Receipt.close).click()







    def confirm_token_page_amount(self, sender_amount):
        logger.info(f"getting amount displayed on token page confirmation modal")
        token_page_amount = self.tokenpage_amount_text()
        amount = sender_amount.strip()
        if token_page_amount == amount:
            logger(f"amount displayed on token page is the correct principal amount")
        else:
            logger(f"amount displayed on token page is not the correct principal amount, expected '{amount}', got '{token_page_amount}'")
        return self.get_text_js(Remittance.tokenpageamount)

    def total_amount(self):
        logger.info(f"getting total amount")
        return self.get_text_js(Remittance.total_amount)

    def click_recipients_country_dropdown(self):
        logger.info(f"clicking country dropdown")
        self.driver.find_element(*Remittance.recipient_country).click()

