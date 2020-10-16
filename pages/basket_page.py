from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException


class BasketPage(BasePage): 

    def should_be_presented_basket_is_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_IS_EMPTY), "There is no text 'Basket is not emppty'"	
        assert True
		
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.TEXT_ITEMS_ARE_IN_BASKET), "There are some items in basket. It should be emppty"	
        assert True