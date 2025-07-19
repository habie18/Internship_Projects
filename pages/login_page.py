from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class LoginPage(Page):

    EMAIL_INPUT = (By.ID, "email-2")
    PASSWORD_INPUT = (By.ID, "field")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[class*='login-button w-button']")

    def login(self, email, password):
        self.type(self.EMAIL_INPUT, 'habeebkassim@outlook.com')
        self.type(self.PASSWORD_INPUT, '@Rasheedat860#')
        sleep(5)
        self.click(self.LOGIN_BUTTON)

