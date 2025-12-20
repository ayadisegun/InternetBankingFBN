from selenium.webdriver.common.by import By
from Utilities.configReader import readconfig
from Utilities.logger import get_logger
from base.baseClass import BaseUtils

logger = get_logger(__name__)

class SecurityQuestion(BaseUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    security_question = (By.XPATH, readconfig("Security_question_page", "security_question"))
    ERROR_MESSAGE_TEXT = (By.XPATH, "//*//div[contains(text(),'Incorrect answer, please try again.')]") #  //div[@class='Toastify']/div/div/div/div[contains(text(),'Incorrect answer, please try again.')]")
    security_page_identifier = (By.XPATH, "//h2[normalize-space()='Security Questions']")
    security_answer = (By.XPATH, readconfig("Security_question_page", "security_answer"))
    proceed = (By.XPATH, readconfig("Security_question_page", "proceed_button"))

    def security_question_text(self):
        return self.driver.find_element(*SecurityQuestion.security_question).text

    def enter_security_answer(self, answer):
        logger.info(f"Entering security answer")
        element = self.driver.find_element(*SecurityQuestion.security_answer)
        element.send_keys(answer)

    def clear_security_answer(self):
        logger.info(f"Clearing security answer")
        answer_field = self.driver.find_element(*SecurityQuestion.security_answer)
        answer_field.click()
        answer_field.clear()
        # self.driver.refresh()

    def click_proceed_button(self):
        logger.info(f"Clicking 'Proceed to Dashboard button'")
        self.driver.find_element(*SecurityQuestion.proceed).click()

    def verify_security_page_access_message_is_displayed(self):
        if self.is_element_visible(self.security_page_identifier):
            print("page identifier is visible.")
        else:
            print("page identifier is not visible.")

    def verify_proceed_button_disabled(self):
        is_disabled = self.check_element_state(self.proceed, "disabled")
        assert is_disabled, "Login button is not disabled as expected"
        print(f"Is button ready to click? {is_disabled}")
        logger.info("Login button is disabled as expected")

    def verify_proceed_button_enabled(self):
        is_enabled = self.check_element_state(self.proceed, "enabled")
        assert is_enabled, "Login button is not disabled as expected"
        print(f"Is button ready to click? {is_enabled}")
        logger.info("Login button is enabled as expected")

    def compare_error_message(self):
        actual_text = self.driver.find_element(*SecurityQuestion.ERROR_MESSAGE_TEXT).text.strip()
        logger.info(f" actual is: '{actual_text}'")
        text_locator = SecurityQuestion.ERROR_MESSAGE_TEXT
        expected_text = "Incorrect answer, please try again."
        is_match = self.compare_text(text_locator, expected_text)
        if not is_match:
            logger.error(f"Error message did not match. Expected: '{expected_text}', Actual: '{actual_text}'")
            assert False, f"Expected '{expected_text}' but got '{actual_text}'"
        logger.info(f"text matched")

    def answer_security_question(self):
        QA_MAP = {
            "what is your favourite city?": "lagos",
            "what is your first school name?": "High school",
            "what is your grandfather's occupation?": "farmer",
        }
        security_question_text = self.security_question_text().lower().strip()
        answer = QA_MAP.get(security_question_text)
        if answer:
            logger.info(f"Answering security question: '{security_question_text}'")
            self.enter_security_answer(answer)
        else:
            utils.get_screenshot("unknown_security_question")
            logger.warning(f"Unknown security question: '{security_question_text}'")

