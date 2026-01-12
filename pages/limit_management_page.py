from locators import LimitManagementLocators
from base.baseClass import BaseUtils
from Utilities.logger import get_logger


logger = get_logger(__name__)

class LimitRequestPage(BaseUtils):

    def create_limit(self, amount):
        logger.info("Creating limit request")
        self.type(LimitManagementLocators.ENTER_LIMIT_INPUT, amount)
        self.click(LimitManagementLocators.CHANGE_LIMIT_BTN)

        # Scroll and handle checkbox
        # self.scroll_to_bottom()
        self.scroll_to_element(LimitManagementLocators.TERMS_CHECKBOX)
        self.driver.find_element(*LimitManagementLocators.TERMS_CHECKBOX).click()
        self.click(LimitManagementLocators.CLOSE_DIALOG_BTN)

    def click_limit_management_menu(self):
        logger.info("Clicking limit management menu")
        self.click(LimitManagementLocators.SELF_SERVICE_MENU)
        self.click(LimitManagementLocators.LIMIT_MGMT_BUTTON)

    def click_back_to_home_button(self):
        logger.info("Clicking back to home button")
        self.click(LimitManagementLocators.BACK_TO_HOME_BUTTON)

    def validate_limit_success(self):
        logger.info("Validating limit success")
        act_text = self.get_text(LimitManagementLocators.SUCCESS_MESSAGE)
        exp_text = "Limit Changed Successfully"
        success_message_detail = self.get_text(LimitManagementLocators.CHANGED_LIMIT_DETAIL)
        self.compare_text(LimitManagementLocators.SUCCESS_MESSAGE, exp_text)
        return print(success_message_detail)

    def enter_token(self, token):
        logger.info("inputting token")
        self.type(LimitManagementLocators.TOKEN_BOX, token)
        self.click(LimitManagementLocators.SUBMIT_BTN)
