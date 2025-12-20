from selenium.webdriver.common.by import By
from Utilities.configReader import readconfig
from Utilities.logger import get_logger


class Transfer:

    def __init__(self, driver):
        self.driver = driver

    accountnumber = (By.XPATH, readconfig("transfer_page", "account_number"))
    receivername = (By.XPATH, readconfig("transfer_page", "receiver_name"))
    amounts = (By.XPATH, readconfig("transfer_page", "amount"))
    narrations = (By.XPATH, readconfig("transfer_page", "narration"))
    proceedbutton = (By.XPATH, readconfig("transfer_page", "proceed"))
    tokenbox = (By.XPATH, readconfig("transfer_page", "token_box"))
    maketransfer = (By.XPATH, readconfig("transfer_page", "make_transfer"))
    generatereceipt = (By.XPATH, readconfig("transfer_page", "generate_receipt"))
    downloadreceipt = (By.XPATH, readconfig("transfer_page", "download_receipt"))
    closereceipt = (By.XPATH, readconfig("transfer_page", "close_receipt"))

    def account_number(self, account_number):
        return self.driver.find_element(*Transfer.accountnumber).send_keys(account_number)

    def get_receiver_name_text(self):
        element = self.driver.find_element(*Transfer.receivername)
        receiver_name_text = element.text
        return receiver_name_text

    def amount(self, amount):
        return self.driver.find_element(*Transfer.amounts).send_keys(amount)

    def narration(self, narration):
        return self.driver.find_element(*Transfer.narrations).send_keys(narration)

    def proceed_button(self):
        return self.driver.find_element(*Transfer.proceedbutton).click()

    def token_box(self, token):
        return self.driver.find_element(*Transfer.tokenbox).send_keys(token)

    def make_transfer(self):
        return self.driver.find_element(*Transfer.maketransfer).click()

    def generate_receipt(self):
        return self.driver.find_element(*Transfer.generatereceipt).click()

    def download_receipt(self):
        return self.driver.find_element(*Transfer.downloadreceipt).click()

    def close_receipt(self):
        self.driver.find_element(*Transfer.closereceipt).click()
        from POM.dashboard_page import Dashboard
        dashboard = Dashboard(self.driver)
        return dashboard

    #
    # def proceed_button(self):
    #     return self.driver.find_element(*Remittance.proceedbutton)

# selectcountrysearchresult = //p[contains(normalize-space(),'')]
# selectbanksearchresult = //p[contains(normalize-space(),'Bank of Ghana')]