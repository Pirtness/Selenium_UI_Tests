from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        email_input.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1_FIELD)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2_FIELD)
        password2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), f"Register form is not presented"
