from selenium.webdriver.common.by import By
from Utilities.configReader import readconfig
from Utilities.logger import get_logger


class BillsPayment:

    def __init__(self, driver):
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