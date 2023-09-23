from selenium.webdriver.common.by import By

"""
Selectors for Sauce Web logged in user state
"""


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
    REMOVE_CART = (By.ID, "remove-sauce-labs-backpack")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")


class SauceWebLoggedInSelectors(object):
    HEADER_CONTAINER = (By.ID, "header_container")


class SauceWebBurgerMenuSelectors(object):
    BURGER_MENU = (By.CSS_SELECTOR, ".bm-burger-button")
    ALL_ITEMS = (By.ID, "inventory_sidebar_link")
    ABOUT = (By.ID, "about_sidebar_link")
    LOGOUT = (By.ID, "logout_sidebar_link")
    RESET_APP = (By.ID, "reset_sidebar_link")


class SauceWebCategoriesSelectors(object):
    CATEGORIES = (By.CLASS_NAME, "product_sort_container")
    Z_A_CATEGORIE = (By.CLASS_NAME, "product_sort_container")


class SauceWebFooterSelectors(object):
    FOOTER = (By.CSS_SELECTOR, ".footer")


class SauseWebErrorMsg(object):
    ERROR_MSG = (By.ID, "logout_sidebar_link")


class SauseWebBodyItemSelectors(object):
    FIRST_ITEM = (By.ID, "item_4_title_link")
    SECOND_ITEM = (By.ID, "item_0_title_link")
    THIRD_ITEM = (By.ID, "item_1_title_link")
    FORTH_ITEM = (By.ID, "item_5_title_link")
    FIFTH_ITEM = (By.ID, "item_2_title_link")
    SIXTH_ITEM = (By.ID, "item_3_title_link")
    INVENTORY_NAME = (By.CLASS_NAME, "inventory_item_name")
    BACKPACK = (By.XPATH, "//*[contains(text(), 'Sauce Labs Backpack')]")
    BOLT_TSHIRT = (By.XPATH, "//*[contains(text(), 'Sauce Labs Bolt T-Shirt')]")
    BIKE_LIGHT = (By.XPATH, "//*[contains(text(), 'Sauce Labs Bike Light')]")
    FLEECE_JACKET = (By.XPATH, "//*[contains(text(), 'Sauce Labs Fleece Jacket')]")
    ONESIE = (By.XPATH, "//*[contains(text(), 'Sauce Labs Onesie')]")
    RED_TSHIRT = (By.XPATH, "//*[contains(text(), 'Test.allTheThings() T-Shirt (Red)')]")
    ITEM_TEXT = (By.CSS_SELECTOR, '.inventory_details_name')
    BACK_NAVIGATION = (By.ID, 'back-to-products')


class SauseWebLogoSelectors(object):
    LOGO = (By.CLASS_NAME, 'header_label')

