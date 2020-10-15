from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")
	
class ProductPageLocators():
	ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	
	ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
	ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
	
	ALLERT_ITEM_ADDED = (By.CSS_SELECTOR, ".alertinner strong")
	ALLERT_BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")

	SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success") 