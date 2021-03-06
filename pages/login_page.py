from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    
    def should_be_login_url(self):
        # assert self.browser.current_url.count('/login/'), "Login is not presented in URL"
        assert '/login/' in self.browser.current_url, "URL does not contains login"
        assert True
    
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "Login form is not presented"
        assert True
    
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTER), "Register for is not presented"
        assert True
		
    def register_new_user(self, email, password):
	    email_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL_INPUT).send_keys(email)
	    password_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_INPUT).send_keys(password)
	    confirm_password_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD_INPUT).send_keys(password)
	    register_button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_REGISTER_BUTTON).click()
