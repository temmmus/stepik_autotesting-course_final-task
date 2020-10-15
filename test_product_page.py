import pytest

from pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear2019"

product_base_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

# @pytest.mark.parametrize('link', urls)
# def test_guest_can_add_product_to_basket(browser, link):
    # page = ProductPage(browser, link)
    # page.open()
    
    # page.should_be_add_to_basket_button()
    # page.add_item_to_basket_button()
    # page.solve_quiz_and_get_code()
    # page.should_be_alert_messages()
		
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, link)
    page.open()

    page.add_item_to_basket_button()
    page.should_not_be_success_message()
      
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    
    page.should_not_be_success_message()
	
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    
    page.add_item_to_basket_button()
    page.is_disappeared()