from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config.config import TestData

"""This parent of all pages classes"""


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.BASE_URL)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_key(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    def is_enabled(self, by_locator):
        return bool(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)))

    def get_title(self, title):
        return WebDriverWait(self.driver, 10).until(EC.title_is(title))
