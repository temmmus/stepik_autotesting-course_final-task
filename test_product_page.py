import pytest
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/queen-of-angels_86/"
	
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

@pytest.mark.parametrize('link', urls)
@pytest.mark.xfail(reason="expected bug")
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_item_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_alert_messages()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket_button()
    page.should_not_be_success_message()
	
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket_button()
    page.is_disappeared()
	
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, link)
    basket_page.should_be_presented_basket_is_empty_text()
    basket_page.should_not_be_items_in_basket()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
		


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser): 
        email = str(time.time()) + "@test.org"
        password = "great_secure_password"
        page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/accounts/login/')
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()
		
    @pytest.mark.need_review	
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        page.add_item_to_basket_button()
        page.should_be_alert_messages()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
		