from selenium.webdriver.common.by import By
from Utilities.configReader import readconfig
from Utilities.logger import get_logger


class TransactionsRequest:

    def __init__(self, driver):
        self.driver = driver

    serviceset = (By.XPATH, readconfig("dashboard_page", "service_setting"))
    header = (By.XPATH, readconfig("dashboard_page", "settings_label"))
    merchant = (By.XPATH, readconfig("service_settings_page", "select_merchant"))


    def set_service(self):
        return self.driver.find_element(*TransactionsRequest.serviceset)

    def click_dashboard(self):
        self.driver.find_element(*TransactionsRequest.dashbd).click()
        from POM.dashboard_page import Dashboard
        dashboard = Dashboard(self.driver)
        return dashboard

    def switchsubmit_button(self):
        return self.driver.find_element(*TransactionsRequest.submitbut)

