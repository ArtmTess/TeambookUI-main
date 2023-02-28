import time
from .base_page import BasePage
from .locators import LoginPageLocators
from .settings import ADMIN_VALID_EMAIL, ADMIN_VALID_PASSWORD


class LoginPage(BasePage):
    def go_to_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(ADMIN_VALID_EMAIL)
        time.sleep(3)

    def go_to_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(ADMIN_VALID_PASSWORD)
        time.sleep(3)

    def go_to_login_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()


