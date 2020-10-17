from selenium.webdriver.common.by import By


class BasePageLocators():
    LINK_LOGIN = (By.CSS_SELECTOR, "#login_link")
    LINK_LOGIN_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET =  (By.XPATH ,"//a[contains(@href, 'basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
	
class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTER = (By.CSS_SELECTOR, "#register_form")
	
    REGISTER_FORM_EMAIL_INPUT = (By.NAME, "registration-email")
    REGISTER_FORM_PASSWORD_INPUT = (By.NAME, "registration-password1")
    REGISTER_FORM_CONFIRM_PASSWORD_INPUT = (By.NAME, "registration-password2")
    REGISTER_FORM_REGISTER_BUTTON = (By.NAME, "registration_submit")
	
class ProductPageLocators():
	BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	
	ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
	ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
	
	ALLERT_ITEM_ADDED = (By.CSS_SELECTOR, ".alertinner strong")
	ALLERT_BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")

	SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success") 
	
class BasketPageLocators():
    # TEXT_BASKET_IS_EMPTY = (By.XPATH ,"//p[contains(text(), 'Ваша корзина пуста')]")
    # TEXT_ITEMS_ARE_IN_BASKET = (By.XPATH , "//h2[contains(text(), 'Товары в корзине')]")
    TEXT_BASKET_IS_EMPTY = (By.XPATH ,"//p[contains(text(), 'Your basket is empty')]")
    TEXT_ITEMS_ARE_IN_BASKET = (By.XPATH , "//h2[contains(text(), 'Items to buy now')]")
