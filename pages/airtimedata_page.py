from selenium.webdriver.common.by import By
from Utilities.configReader import readconfig
from Utilities.logger import get_logger


class AirtimeData:

    def __init__(self, driver):
        self.driver = driver

    network_provider = (By.XPATH, readconfig("airtimedata_page", "network_provider"))
    airteldata_option = (By.XPATH, readconfig("airtimedata_page", "airteldata_option"))
    mtndata_option = (By.XPATH, readconfig("airtimedata_page", "mtndata_option"))
    glodata_option = (By.XPATH, readconfig("airtimedata_page", "glodata_option"))
    ninemobiledata_option = (By.XPATH, readconfig("airtimedata_page", "mobiledata_option"))
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

    def select_network_provider(self):
        return self.driver.find_element(*AirtimeData.network_provider)

    def airteldata(self):
        return self.driver.find_element(*AirtimeData.airteldata_option)

    def mtndata(self):
        return self.driver.find_element(*AirtimeData.mtndata_option)

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

