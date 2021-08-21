import time

from selenium.webdriver.common.by import By

from Pages.Base import Base


class LoginPage(Base):
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    LOGIN_BUTTON = (By.NAME, "login")
    SIGNUP_LINK = (By.LINK_TEXT, "Create New Account")

    def __init__(self, driver):
        super().__init__(driver)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_signup_link_exists(self):
        return self.is_enabled(self.SIGNUP_LINK)

    def do_login(self, username, password):
        self.do_send_key(self.EMAIL, username)
        self.do_send_key(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
