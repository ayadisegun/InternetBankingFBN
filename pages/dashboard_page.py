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


    SELF_SERVICE_MENU = (By.XPATH, "//a/span[contains(.,'Self Service')]")
    USER_DASHBOARD_PAGE_IDENTIFIER = (By.XPATH, "//span[contains(text(), 'Transaction Requests')]")
    TRANSFER_MENU = (By.XPATH, "//span[contains(text(), 'Transfer')]")
    OWN_ACCOUNT_OPTION = (By.XPATH, "//a[contains(text(), 'Own Account')]")
    OTHER_BANKS_OPTION = (By.XPATH, "//a[contains(text(), 'Other Banks')]")
    FIRST_BANK_OPTION = (By.XPATH, "//a[contains(text(), 'FirstBank')]")
    AIRTIME_AND_DATA_OPTION = (By.XPATH, "//span[contains(text(), 'Airtime and Data')]")
    BILLS_PAYMENT_OPTION = (By.XPATH, "//span[contains(text(), 'Bills Payment')]")
    BUY_AIRTIME_OPTION = (By.XPATH, "//a[contains(text(), 'Buy Airtime')]")
    BUY_DATA_OPTION = (By.XPATH, "//a[contains(text(), 'Buy Data')]")
    LOGOUT = (By.XPATH, "//span[contains(text(), 'Logout')]")
    LOGOUT_CONFIRMATION = (By.XPATH, "//button[contains(text(), 'Yes')]")

    # Actions
    def click_transfer_menu(self):
        logger.info("Clicking Transfer menu")
        self.click(self.TRANSFER_MENU)


    def click_own_account_option(self):
        logger.info("Clicking Own Account option")
        self.click(self.OWN_ACCOUNT_OPTION)

    def click_first_bank_account_option(self):
        logger.info("Clicking FirstBank option")
        self.click(self.FIRST_BANK_OPTION)

    def click_other_bank_account_option(self):
        logger.info("Clicking Other Banks option")
        self.click(self.OTHER_BANKS_OPTION)

    def click_airtime_and_data_option(self):
        logger.info("Clicking Airtime and Data option")
        # self.click(self.AIRTIME_AND_DATA_OPTION)
        self.driver.find_element(*self.AIRTIME_AND_DATA_OPTION).click()
        self.wait_for_seconds(2)


    def click_buy_airtime_option(self):
        logger.info("Clicking Buy Airtime option")
        # self.click(self.BUY_AIRTIME_OPTION)
        self.driver.find_element(*self.BUY_AIRTIME_OPTION).click()
        self.wait_for_seconds(2)

    def click_buy_data_option(self):
        logger.info("Clicking Buy Data option")
        self.click(self.BUY_DATA_OPTION)

    def click_bills_payment_option(self):
        logger.info("Clicking bills payment option")
        self.click(self.BILLS_PAYMENT_OPTION)

    def click_and_confirm_logout(self):
        logger.info("Clicking Logout and confirming")
        self.click(self.LOGOUT)
        self.click(self.LOGOUT_CONFIRMATION)

    # Navigation
    def navigate_to_own_account_transfer(self):
        logger.info("Navigating to Own Account Transfer")
        self.click_transfer_menu()
        self.click_own_account_option()

    def navigate_to_first_bank_account_transfer(self):
        logger.info("Navigating to FirstBank Account Transfer")
        self.click_transfer_menu()
        self.click_first_bank_account_option()

    def navigate_to_other_bank_account_transfer(self):
        logger.info("Navigating to Other Bank Account Transfer")
        self.click_transfer_menu()
        self.click_other_bank_account_option()

    def navigate_to_buy_data(self):
        logger.info("Navigating to Data Purchase")
        self.click_airtime_and_data_option()
        self.click_buy_data_option()

    def navigate_to_buy_airtime(self):
        logger.info("Navigating to Airtime Purchase")
        self.click_airtime_and_data_option()
        self.click_buy_airtime_option()

    def navigate_to_bills_payment(self):
        logger.info("Navigating to Bills Payment")
        logger.info("Waiting for Bills Payment Option")
        self.click_bills_payment_option()

    # Verifiers
    def verify_user_dashboard_page_access_message_is_displayed(self):
        visible = self.is_visible(self.USER_DASHBOARD_PAGE_IDENTIFIER)
        assert visible, "User Dashboard page should be visible"
        logger.info("User Dashboard page is displayed successfully")




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

    def buy_data_menu(self):
        self.driver.find_element(*Dashboard.airtime_data).click()
        self.driver.find_element(*Dashboard.buy_data).click()

    def bills_payment_tab(self):
        self.driver.find_element(*Dashboard.bills_payment).click()

    def click_remittance_tab(self):
        self.driver.find_element(*Dashboard.remittance).click()
        # from POM.remittance_page import Remittance
        # remittance = Remittance(self.driver)
        # return remittance

    def sme_loan(self):
        self.driver.find_element(*Dashboard.smeloan).click()

    def transactions_request(self):
        self.driver.find_element(*Dashboard.transactionsrequest).click()
        # from POM.transactions_request_page import TransactionsRequest
        # transactions_request = TransactionsRequest(self.driver)
        # return transactions_request

    def settings_tab(self):
        self.driver.find_element(*Dashboard.settings).click()
        # from POM.settings_page import Settings
        # settings = Settings(self.driver)
        # return settings

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
        self.driver.find_element(*Dashboard.logout).click()

    def confirm_logout(self):
        self.driver.find_element(*Dashboard.log_out_yes).click()

    def click_and_confirm_logout1(self):
        self.driver.find_element(*Dashboard.logout).click()
        self.driver.find_element(*Dashboard.log_out_yes).click()

    def logout_no(self):
        return self.driver.find_element(*Dashboard.log_out_no)

