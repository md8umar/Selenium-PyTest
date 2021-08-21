from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class TestData:
    BASE_URL = "https://en-gb.facebook.com/"
    username = "pracmail78@gmail.com"
    password = "Practice@90"
    Login_PAGE_TITLE = "Facebook – log in or sign up"
