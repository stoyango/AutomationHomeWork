from selenium.webdriver.common.by import By

class SauceWebPurcheseSelectors(object):
    ADD_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    SHOPPING_CART = (By.ID, "shopping_cart_container")
    CHECKOUT = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POST_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    COMLETE = (By.CLASS_NAME, "complete-header")

class SauceWebLoggedIn(object):
    HEADER_CONTAINER = (By.ID, "header_container")

class SauceWebBurgerMenuSelectors(object):
    BURGER_MENU = (By.CSS_SELECTOR, ".bm-burger-button")

class SauceWebFooterSelectors(object):
    FOOTER = (By.CSS_SELECTOR, ".footer")

class SauceWebLogOutSelectors(object):
    LOG_OUT = (By.ID, "logout_sidebar_link")
