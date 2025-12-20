import datetime
import os
from datetime import datetime
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    WebDriverException,
    ElementNotInteractableException
)
import openpyxl
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from Utilities.configReader import readconfig
import re


class BaseUtils:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def get_screenshot(self, filename: str):
        screenshot_dir = readconfig("setup", "screenshot_dir")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.join(screenshot_dir, f"{filename}_{timestamp}.png")
        self.driver.get_screenshot_as_file(path)

    def scroll_to_element(self, element):
        """Scroll to a specific element"""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)

    def scroll_to_bottom(self):
        """Scroll to bottom of page"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_down(self):
        """Scroll by specific pixel amount"""
        self.driver.execute_script("window.scrollBy(0, 300);")

    def scroll_to_top(self):
        """Scroll to top of page"""
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_by_pixels(self, x=0, y=800):
        """Scroll by specific pixel amount"""
        self.driver.execute_script(f"window.scrollBy({x}, {y});")

    def scroll_to_element_by_pixel(self, element):
        self.driver.execute_script("arguments[0].scrollTop += 600;", element)

    def wait_and_click(self, locator, timeout=10):
        """Wait for element and click"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        return element

    def wait_until_present(self, locator):
        mywait = WebDriverWait(self.driver, 10)
        mywait.until(EC.presence_of_element_located(locator))

    # def hover_over_element(self, element):
    #     """Hover over an element"""
    #     ActionChains(self.driver).move_to_element(element).perform()

    def selectoption_bytext(self, locator, text):
        driver = self.driver
        optns = Select(driver.find_element(locator))
        optns.select_by_visible_text(text)

    def mouse_over(self, element):
        ele = self.driver.find_element(element)
        ActionChains(self.driver).move_to_element(ele).perform()

    def double_click(self, element):
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()

    def delete_cookie(self):
        self.driver.delete_all_cookies()

    def delete_session(self):
        self.driver.execute_script("window.sessionStorage.clear();")

    def delete_localstorage(self):
        self.driver.execute_script("window.localStorage.clear();")


    def find_element(self, locator: tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator: tuple):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator: tuple, text: str):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def check_checkbox(self, locator: tuple):
        element = self.find_element(locator)
        if not element.is_selected():
            element.click()

    def text_of_element(self, locator: tuple) -> str:
        return self.find_element(locator).text.strip()

    def is_visible(self, locator: tuple) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def is_element_enabled(self, locator: tuple) -> bool:
        try:
            element = self.find_element(locator)
            return element.is_enabled()
        except Exception:
            return False

    def get_text_js(self, locator: tuple):
        try:
            element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(locator)
            )
            return self.driver.execute_script("return arguments[0].innerText;", element).strip()
        except Exception:
            return ""

    def convert_to_float(self, text):
        # Removes everything except digits and decimal points
        clean_text = re.sub(r'[^\d.]', '', text)
        return float(clean_text) if clean_text else 0.0

    def get_numeric_value(self, text):
        # This finds the first group of numbers, commas, and decimals
        # For '₦ 2,320.40 (Equivalent...)', it captures '2,320.40'
        match = re.search(r'[\d,.]+', text)
        if match:
            clean_string = match.group().replace(',', '')
            return float(clean_string)
        return 0.0

    def compare_text1(self, locator: tuple, expected_text: str) -> bool:
        try:
            actual = self.text_of_element(locator)
            return actual.lower() == expected_text.lower()
        except:
            return False

    def is_attribute_present(self, locator: tuple, attribute: str) -> bool:
        try:
            element = self.find_element(locator)
            value = element.get_attribute(attribute)
            return value is not None
        except:
            return False

    def remove_attribute(self, locator: tuple, attribute: str):
        try:
            element = self.find_element(locator)
            self.driver.execute_script(
                "arguments[0].removeAttribute(arguments[1]);",
                element,
                attribute
            )
        except Exception as e:
            print(f"Error removing attribute '{attribute}': {e}")

    def quit(self):
        self.driver.quit()

    def is_element_visible(self, locator: tuple) -> bool:
        """Checks if an element is present in the DOM and visible on the page."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

    def compare_text(self, locator: tuple, expected_text: str) -> bool:
        """Gets the text of an element and compares it to an expected string."""
        try:
            element_text = self.wait.until(EC.visibility_of_element_located(locator)).text
            return element_text.strip() == expected_text.strip()
        except TimeoutException:
            return False

    def check_element_state(self, locator: tuple, state: str) -> bool:
        """
        Generic state checker.
        Supported states: 'enabled', 'disabled', 'displayed', 'selected'
        """
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            if state.lower() == "enabled":
                return element.is_enabled()
            elif state.lower() == "disabled":
                return not element.is_enabled()
            elif state.lower() == "displayed":
                return element.is_displayed()
            elif state.lower() == "selected":
                return element.is_selected()
            else:
                # Fallback for custom attributes like 'aria-disabled'
                return element.get_attribute(state) is not None
        except TimeoutException:
            return False



class HomepageData:
    homepagetestData = [{"firstname": "segun", "email": "xyz@gmail.com", "password": "password123", "gender": "Male"}, {"firstname": "Ade", "email": "abc@gmail.com", "password": "passwordfemale", "gender": "Female"}]

# Android Keycodes
# 0 - 7
# 1 - 8
# 2 - 9
# 3 - 10
# 4 - 11
# 5 - 12
# 6 - 13
# 7 - 14
# 8 - 15
# 9 -16
# 10 -
# 11 - 227
# 12 - 228
# Shift - 59
# back - 4
# home - 3
# recent app - 187
# driver.launch_app()  # Reopen the app
# driver.background_app(5)  # Minimize the app for 5 seconds
# power key 26
# volume up 24
# volume down 25
#delete - 67
#Enter - (66)

