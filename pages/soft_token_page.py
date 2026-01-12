from locators import SoftTokenLocators
from base.baseClass import BaseUtils
from Utilities.logger import get_logger


logger = get_logger(__name__)

class SoftTokenPage(BaseUtils):
    # Dictionary to handle your security logic
    SECURITY_ANSWERS = {
        "what is your favourite city?": "lagos",
        "what is your first school name?": "High school",
        "what is your grandfather's occupation?": "farmer",
    }

    def answer_security_question(self):
        logger.info("attempting security question")
        # Capture the actual question text from the UI
        question_text = self.get_text(SoftTokenLocators.SECURITY_QUESTION_TEXT).lower()

        # Match question to answer, default to a message if not found
        answer = self.SECURITY_ANSWERS.get(question_text, "Answer not found")

        if answer != "Answer not found":
            self.type(SoftTokenLocators.SECURITY_ANSWER_FIELD, answer)
        else:
            self.get_screenshot("unknown_security_question")
            logger.warning(f"Unknown security question: '{security_question_text}'")
            raise Exception(f"Unknown Security Question: {question_text}")

    def click_soft_token_menu(self):
        logger.info("Clicking soft token menu")
        self.click(SoftTokenLocators.SELF_SERVICE_MENU)
        self.click(SoftTokenLocators.SOFT_TOKEN_BTN)

    def click_back_to_home_button(self):
        logger.info("Clicking back to home button")
        self.click(SoftTokenLocators.BACK_TO_HOME_BUTTON)

    def validate_limit_success(self):
        logger.info("Validating limit success")
        act_text = self.get_text(SoftTokenLocators.SUCCESS_MESSAGE)
        exp_text = "Limit Changed Successfully"
        success_message_detail = self.get_text(SoftTokenLocators.CHANGED_LIMIT_DETAIL)
        self.compare_text(SoftTokenLocators.SUCCESS_MESSAGE, exp_text)
        return print(success_message_detail)

    def enter_token(self, token):
        logger.info("inputting token")
        self.type(SoftTokenLocators.TOKEN_BOX, token)
        self.click(SoftTokenLocators.SUBMIT_BTN)

    def search_and_select_users(self, search_term):
        logger.info("searching users")
        self.type(SoftTokenLocators.SEARCH_FIELD, search_term)
        self.click(SoftTokenLocators.FETCHED_ITEM)

    def click_request_enrolment_button(self):
        logger.info("Clicking request enrolment button")
        self.click(SoftTokenLocators.REQUEST_ENROLLMENT_BTN)