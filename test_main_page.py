import pytest
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage
import time

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
	
        page.should_be_login_link()
        page.go_to_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.should_be_basket_button()
        page.go_to_basket_page()

        basket_page = BasketPage(browser, link)
        basket_page.should_be_presented_basket_is_empty_text()
        basket_page.should_not_be_items_in_basket()
	