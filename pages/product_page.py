from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage): 
		
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Buttom is not presented"
		
    def add_item_to_basket_button(self):	
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_button.click() 
		
    def should_be_alert_messages(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_NAME).text == self.browser.find_element(*ProductPageLocators.ALLERT_ITEM_ADDED).text, "A name in the alert message is different"
		
        assert self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text == self.browser.find_element(*ProductPageLocators.ALLERT_BASKET_TOTAL).text, "A price in the alert message is different"
		
    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"
    		
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    	   
		