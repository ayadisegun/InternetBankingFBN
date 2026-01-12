from selenium.webdriver.common.by import By


class LimitManagementLocators:
    # Limit Management Section
    SELF_SERVICE_MENU = (By.XPATH, "//a/span[contains(.,'Self Service')]")
    LIMIT_MGMT_BUTTON = (By.XPATH, "//a[normalize-space()='Limit Management']")
    HEADER_TEXT = (By.XPATH, "//h2[normalize-space()='Limit Management']")
    ENTER_LIMIT_INPUT = (By.XPATH, "//input[@placeholder='Enter the Limit']")
    CHANGE_LIMIT_BTN = (By.XPATH, "//button[normalize-space()='Change Limit']")
    TERMS_CHECKBOX = (By.XPATH, "//div[@class='flex gap-1 text-[10px]  md:text-[12px] l:text-[14px] items-center  text-center']/div/input[@type='checkbox']")
    CLOSE_DIALOG_BTN = (By.XPATH, "//button[normalize-space()='Close']")

    # Token & Submission
    TOKEN_BOX = (By.XPATH, "//input[@type='password'][1]")
    SUBMIT_BTN = (By.XPATH, "//button[normalize-space()='Change Limit']")
    SOFT_TOKEN_BTN = (By.XPATH, "//a[normalize-space()='Soft Token']")

    #Success page
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(),'Limit Changed Successfully')]")
    CHANGED_LIMIT_DETAIL = (By.XPATH, "(//p[@class='text-[#002855] text-[11px] md:text-[15px] my-3 text-center px-6'])[1]")
    BACK_TO_HOME_BUTTON = (By.XPATH, "//button[normalize-space()='Back To Home']")

class SoftTokenLocators:
    # Search & Enrollment
    SELF_SERVICE_MENU = (By.XPATH, "//a/span[contains(.,'Self Service')]")
    SEARCH_FIELD = (By.XPATH, "//input[@placeholder='Search']")
    FETCHED_ITEM = (By.XPATH, "//div[contains(@class, 'cursor-pointer') and contains(@class, 'bg-[#EFF3FE]')]")
    REQUEST_ENROLLMENT_BTN = (By.XPATH, "//button[normalize-space()='Request Enrollment ID']")

    # Token & Submission
    TOKEN_BOX = (By.XPATH, "//input[@type='password'][1]")
    SUBMIT_BTN = (By.XPATH, "//button[normalize-space()='Change Limit']")
    SOFT_TOKEN_BTN = (By.XPATH, "//a[normalize-space()='Soft Token']")

    # Security Questions
    SECURITY_QUESTION_TEXT = (By.XPATH, "//h4[@class='text-[13px] lg:text-[16px] text-nowrap mb-2']")  # Dynamic capture
    SECURITY_ANSWER_FIELD = (By.XPATH, "//input[@placeholder='Please enter your answer here ']")