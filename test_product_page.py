import pytest
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear2019"
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	
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
	
# def test_message_disappeared_after_adding_product_to_basket(browser):
    # page = ProductPage(browser, link)
    # page.open()
    # page.add_item_to_basket_button()
    # page.is_disappeared()
	
# def test_guest_should_see_login_link_on_product_page(browser):
    # page = ProductPage(browser, link)
    # page.open()
    # page.should_be_login_link()
		
# def test_guest_can_go_to_login_page_from_product_page(browser):
    # page = ProductPage(browser, link)
    # page.open()
    # page.go_to_login_page()
	
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, link)
    basket_page.should_be_presented_basket_is_empty_text()
    basket_page.should_not_be_items_in_basket()