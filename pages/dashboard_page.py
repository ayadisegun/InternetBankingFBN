import time

from selenium.webdriver.common.by import By
from base.baseClass import BaseUtils
from Utilities.configReader import readconfig
from Utilities.logger import get_logger

logger = get_logger(__name__)

class Dashboard(BaseUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    dashboard = (By.XPATH, readconfig("dashboard_page", "dashboard_tab"))
    airtime_data = (By.XPATH, readconfig("dashboard_page", "airtime_data"))
    buy_airtime = (By.XPATH, readconfig("dashboard_page", "buy_airtime"))
    buy_data = (By.XPATH, readconfig("dashboard_page", "buy_data"))
    bills_payment = (By.XPATH, readconfig("dashboard_page", "bills_payment"))
    remittance = (By.XPATH, readconfig("dashboard_page", "remittance"))
    smeloan = (By.XPATH, readconfig("dashboard_page", "sme_loan"))
    transactionsrequest = (By.XPATH, readconfig("dashboard_page", "transactions_request"))
    settings = (By.XPATH, readconfig("dashboard_page", "settings"))
    profileicon = (By.XPATH, readconfig("dashboard_page", "profile_icon"))
    profilesettings = (By.XPATH, readconfig("dashboard_page", "profile_settings"))
    logout = (By.XPATH, readconfig("dashboard_page", "logout"))
    log_out_yes = (By.XPATH, readconfig("dashboard_page", "logout_yes"))
    log_out_no =(By.XPATH, readconfig("dashboard_page", "logout_no"))
    transfertab = (By.XPATH, readconfig("dashboard_page", "transfer_tab"))
    firstbank = (By.XPATH, readconfig("dashboard_page", "first_bank"))
    ownaccount = (By.XPATH, readconfig("dashboard_page", "own_account"))
    otherbanks = (By.XPATH, readconfig("dashboard_page", "other_banks"))
    bulktransfer = (By.XPATH, readconfig("dashboard_page", "bulk_transfer"))

    def dashboard_tab(self):
        return self.driver.find_element(*Dashboard.dashboard)

    def verify_dashboard_page_is_displayed(self):
        if self.is_element_visible(self.dashboard):
            logger.info("Dashboard page is displayed")
        else:
            logger.info("Dashboard page is not displayed")

    def verify_login_page_access_message_is_displayed(self):
        # 1. Check Visibility
        if self.is_element_visible(self.LOGIN_PAGE_IDENTIFIER):
            print("page identifier is visible.")
        else:
            print("page identifier is not visible.")

    def buy_airtime_menu(self):
        self.driver.find_element(*Dashboard.airtime_data).click()
        self.driver.find_element(*Dashboard.buy_airtime).click()
        from POM.airtimedata_page import AirtimeData
        airtimeData = AirtimeData(self.driver)
        return airtimeData

    def buy_data_menu(self):
        self.driver.find_element(*Dashboard.airtime_data).click()
        self.driver.find_element(*Dashboard.buy_data).click()
        from POM.airtimedata_page import AirtimeData
        airtimeData = AirtimeData(self.driver)
        return airtimeData

    def bills_payment_tab(self):
        self.driver.find_element(*Dashboard.bills_payment).click()
        from POM.bills_payment_page import  BillsPayment
        bills_payment = BillsPayment(self.driver)
        return bills_payment

    def click_remittance_tab(self):
        self.driver.find_element(*Dashboard.remittance).click()
        # from POM.remittance_page import Remittance
        # remittance = Remittance(self.driver)
        # return remittance

    def sme_loan(self):
        self.driver.find_element(*Dashboard.smeloan).click()
        from POM.sme_loan_page import SmeLoan
        sme_loan = SmeLoan(self.driver)
        return sme_loan

    def transactions_request(self):
        self.driver.find_element(*Dashboard.transactionsrequest).click()
        from POM.transactions_request_page import TransactionsRequest
        transactions_request = TransactionsRequest(self.driver)
        return transactions_request

    def settings_tab(self):
        self.driver.find_element(*Dashboard.settings).click()
        from POM.settings_page import Settings
        settings = Settings(self.driver)
        return settings

    def transfer_tab(self):
        return self.driver.find_element(*Dashboard.transfertab).click()

    def first_bank(self):
        self.driver.find_element(*Dashboard.firstbank).click()
        from POM.transfer_page import Transfer
        transfer = Transfer(self.driver)
        return transfer

    def own_account(self):
        self.driver.find_element(*Dashboard.ownaccount).click()
        from POM.transfer_page import Transfer
        transfer = Transfer(self.driver)
        return transfer

    def other_banks(self):
        self.driver.find_element(*Dashboard.otherbanks).click()
        from POM.transfer_page import Transfer
        transfer = Transfer(self.driver)
        return transfer

    def bulk_transfer(self):
        self.driver.find_element(*Dashboard.bulktransfer).click()
        from POM.transfer_page import Transfer
        transfer = Transfer(self.driver)
        return transfer

    def profile_icon(self):
        return self.driver.find_element(*Dashboard.profileicon)

    def profile_settings(self):
        return self.driver.find_element(*Dashboard.profilesettings)

    def click_logout_tab(self):
        return self.driver.find_element(*Dashboard.logout)

    def confirm_logout(self):
        self.driver.find_element(*Dashboard.log_out_yes).click()

    def logout_no(self):
        return self.driver.find_element(*Dashboard.log_out_no)

