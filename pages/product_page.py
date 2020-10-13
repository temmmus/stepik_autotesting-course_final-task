from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage): 
		
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Buttom is not presented"
		
    def add_item_to_basket_button(self):	
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click() 
		
    def should_be_alert_messages(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_NAME).text == self.browser.find_element(*ProductPageLocators.ALLERT_ITEM_ADDED).text, "A name in the alert message is different"
		
        assert self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text == self.browser.find_element(*ProductPageLocators.ALLERT_BASKET_TOTAL).text, "A price in the alert message is different"
		