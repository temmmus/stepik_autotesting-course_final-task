from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage): 
		
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Buttom is not presented"
		
    def add_item_to_basket_button(self):	
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click() 
		
    def should_be_alert_messages(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_NAME).text == self.browser.find_element(*ProductPageLocators.ALLERT_ITEM_ADDED).text, "A name in the alert message is different"
		
        assert self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text == self.browser.find_element(*ProductPageLocators.ALLERT_BASKET_TOTAL).text, "A price in the alert message is different"
		
    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"
    		
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
    
        return False
    	
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    	   
    	   
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
    
        return True