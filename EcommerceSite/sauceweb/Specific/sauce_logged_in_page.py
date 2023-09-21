from selenium.webdriver.common.by import By
from EcommerceSite.sauceweb.Specific.sauce_logged_in_page_selectors import SauceWebPurcheseSelectors, \
    SauceWebBurgerMenuSelectors, SauceWebLoggedInSelectors, SauceWebFooterSelectors,\
    SauseWebBodyItemSelectors, SauseWebLogoSelectors, SauseWebErrorMsg, SauceWebCategoriesSelectors
from selenium.webdriver.support.ui import Select

class LoggedInPage():
    def __init__(self, driver):
        self.driver = driver


    def is_header_logged_displayed(self):
        if self.driver.find_element(*SauceWebLoggedInSelectors.HEADER_CONTAINER).is_displayed():
            print('header presented')
        else:
            print('header not presented')

    def purchase_item_flow(self, username, password, zipcode):
        try:
            self.driver.find_element(*SauceWebPurcheseSelectors.ADD_CART).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.SHOPPING_CART).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.CHECKOUT).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.FIRST_NAME).send_keys(username)
            self.driver.find_element(*SauceWebPurcheseSelectors.LAST_NAME).send_keys(password)
            self.driver.find_element(*SauceWebPurcheseSelectors.POST_CODE).send_keys(zipcode)
            self.driver.find_element(*SauceWebPurcheseSelectors.CONTINUE).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.FINISH).click()
            if self.driver.find_element(*SauceWebPurcheseSelectors.COMLETE).is_displayed():
                print('complete presented')
            else:
                print('complete not presented')
        except:
            raise Exception ('')

    def deposit_methods_availability(self):
        """
        This method compares and checks if the expected Payment methods for deposit
        for CC IE geo and these displayed on the site are the same.
        """
        all_spans = self.driver.find_elements(*SauseWebBodyItemSelectors.INVENTORY_NAME)
        for span in all_spans:
            print(span.text)
        expected_payment_methods = ['Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Onesie', 'Sauce Labs Fleece Jacket',
                                    'Sauce Labs Bolt T-Shirt', 'Sauce Labs Bike Light','Sauce Labs Backpack']
        available_payment_methods = self.driver.find_elements(*SauseWebBodyItemSelectors.INVENTORY_NAME)
        print(available_payment_methods)
        if expected_payment_methods == available_payment_methods:
            return True
        else:
            return False
    def is_error_message_displayed(self):
        return self.driver.find_element(*SauseWebErrorMsg.ERROR_MSG)

    def purchase_item__no_user_data_flow(self):
        try:
            self.driver.find_element(*SauceWebPurcheseSelectors.ADD_CART).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.SHOPPING_CART).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.CHECKOUT).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.CONTINUE).click()
        except:
            raise Exception ('')

    def logout_flow(self):
        try:
            self.click_burger_menu()
            self.driver.find_element(*SauceWebBurgerMenuSelectors.LOGOUT).click()
        except:
            raise Exception ('')

    def click_burger_menu(self):
        try:
            self.driver.find_element(*SauceWebBurgerMenuSelectors.BURGER_MENU).click()
        except:
            raise Exception ('')

    def click_categories_menu(self):
        try:
            self.driver.find_element(*SauceWebCategoriesSelectors.CATEGORIES).click()
        except:
            raise Exception ('')

    def click_categories_z_a_menu(self):
        try:
            select = Select(self.driver.find_element(*SauceWebCategoriesSelectors.CATEGORIES))
            select.select_by_value('za')
        except:
            raise Exception ('')

    def is_footer_displayed(self):
        if self.driver.find_element(*SauceWebFooterSelectors.FOOTER).is_displayed():
            print('footer presented')
        else:
            print('footer not presented')

    def is_all_items_displayed(self):
        return self.driver.find_element(*SauceWebBurgerMenuSelectors.ALL_ITEMS)

    def is_about_displayed(self):
        return self.driver.find_element(*SauceWebBurgerMenuSelectors.ABOUT)

    def is_logout_displayed(self):
        return self.driver.find_element(*SauceWebBurgerMenuSelectors.LOGOUT)

    def is_reset_app_displayed(self):
        return self.driver.find_element(*SauceWebBurgerMenuSelectors.RESET_APP)

    def is_all_burger_menu_items_displayed(self):
        """
        This method checks for visibility of banner's elements
        :return: True or False
        """
        body_items = [self.is_all_items_displayed(), self.is_about_displayed(),
                      self.is_logout_displayed(), self.is_reset_app_displayed()]
        error_count = 0
        for method in body_items:
            if method is False:
                error_count += 1
        if error_count > 0:
            return False
        else:
            return True

    def add_cart_flow(self):
        self.driver.find_element(*SauceWebPurcheseSelectors.ADD_CART).click()
        self.driver.find_element(*SauceWebPurcheseSelectors.SHOPPING_CART).click()

    def is_added_item_displayed(self):
        if self.driver.find_element(*SauceWebPurcheseSelectors.REMOVE_CART).is_displayed():
            print('footer presented')
        else:
            print('footer not presented')

    def remove_cart_flow(self):
        self.driver.find_element(*SauceWebPurcheseSelectors.REMOVE_CART).click()
        self.driver.find_element(*SauceWebPurcheseSelectors.CONTINUE_SHOPPING).click()

    def is_first_item_displayed(self):
        if self.driver.find_element(*SauseWebBodyItemSelectors.FIRST_ITEM).is_displayed():
            print('Backpack presented')
        else:
            print('Backpack not presented')

    def is_second_item_displayed(self):
        if self.driver.find_element(*SauseWebBodyItemSelectors.SECOND_ITEM).is_displayed():
            print('Bike Light presented')
        else:
            print('Bike Light not presented')

    def is_third_item_displayed(self):
        if self.driver.find_element(*SauseWebBodyItemSelectors.THIRD_ITEM).is_displayed():
            print('Bolt T-Shirt presented')
        else:
            print('Bolt T-Shirt not presented')

    def is_forth_Item_displayed(self):
        if self.driver.find_element(*SauseWebBodyItemSelectors.FORTH_ITEM).is_displayed():
            print('Jacket presented')
        else:
            print('Jacket not presented')

    def is_fifth_item_displayed(self):
        if self.driver.find_element(*SauseWebBodyItemSelectors.FIFTH_ITEM).is_displayed():
            print('Onesie presented')
        else:
            print('Onesie not presented')

    def is_sixth_item_displayed(self):
        if self.driver.find_element(*SauseWebBodyItemSelectors.SIXTH_ITEM).is_displayed():
            print('T-Shirt presented')
        else:
            print('T-Shirt not presented')

    def is_all_body_items_displayed(self):
        """
        This method checks for visibility of banner's elements
        :return: True or False
        """
        body_items = [self.is_fifth_item_displayed(), self.is_sixth_item_displayed(),
                      self.is_forth_Item_displayed(), self.is_third_item_displayed(),
                      self.is_second_item_displayed(), self.is_first_item_displayed()]
        error_count = 0
        for method in body_items:
            if method is False:
                error_count += 1
        if error_count > 0:
            return False
        else:
            return True

        # Method will check for live balance image
    def get_logo_text(self):
        return self.driver.find_element(*SauseWebLogoSelectors.LOGO).text

    # Method will compare actual and expected text
    def check_logo_text(self):
        if self.get_logo_text() == "Swag Labs":
            return True
        else:
            return False



