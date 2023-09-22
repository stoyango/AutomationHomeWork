from EcommerceSite.sauceweb.Specific.sauce_logged_in_page_selectors import SauceWebPurcheseSelectors, \
    SauceWebBurgerMenuSelectors, SauceWebLoggedInSelectors, SauceWebFooterSelectors,\
    SauseWebBodyItemSelectors, SauseWebLogoSelectors, SauseWebErrorMsg, SauceWebCategoriesSelectors
from selenium.webdriver.support.ui import Select


class LoggedInPage:
    def __init__(self, driver):
        self.driver = driver

    def is_header_logged_displayed(self):
        """
        Method will check if element is displayed
        """
        if self.driver.find_element(*SauceWebLoggedInSelectors.HEADER_CONTAINER).is_displayed():
            print('Header is presented')
        else:
            print('Header is not presented')

    def purchase_item_flow(self, username, password, zipcode):
        """
        Method will verify purchase flow
        """
        try:
            self.driver.find_element(*SauceWebPurcheseSelectors.ADD_CART).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.SHOPPING_CART).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.CHECKOUT).click()
            print('Add Cart, Shopping Cart and Checkout are clicked')
            self.driver.find_element(*SauceWebPurcheseSelectors.FIRST_NAME).send_keys(username)
            self.driver.find_element(*SauceWebPurcheseSelectors.LAST_NAME).send_keys(password)
            self.driver.find_element(*SauceWebPurcheseSelectors.POST_CODE).send_keys(zipcode)
            print('User data was filled')
            self.driver.find_element(*SauceWebPurcheseSelectors.CONTINUE).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.FINISH).click()
            if self.driver.find_element(*SauceWebPurcheseSelectors.COMLETE).is_displayed():
                print('Purchase flow completed')
            else:
                print('Purchase flow not completed')
        except:
            raise Exception('Was not able to proceed with purchase flow')

    def add_cart_flow(self):
        """
        Method will check add cart functionality
        """
        try:
            self.driver.find_element(*SauceWebPurcheseSelectors.ADD_CART).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.SHOPPING_CART).click()
            print('Add cart flow completed')
        except:
            raise Exception('Add cart flow was not completed')

    def remove_cart_flow(self):
        """
        Method will check remove cart functionality
        """
        try:
            self.driver.find_element(*SauceWebPurcheseSelectors.REMOVE_CART).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.CONTINUE_SHOPPING).click()
            print('Remove cart flow completed')
        except:
            raise Exception('Remove cart flow not completed')

    def is_error_message_displayed(self):
        """
        Method will check if element is displayed
        """
        return self.driver.find_element(*SauseWebErrorMsg.ERROR_MSG)

    def purchase_item_no_user_data_flow(self):
        """
        Method will verify purchase flow with no data provided
        """
        try:
            self.driver.find_element(*SauceWebPurcheseSelectors.ADD_CART).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.SHOPPING_CART).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.CHECKOUT).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.CONTINUE).click()
            print('Add Cart, Shopping Cart and Checkout and Continue were clicked')
        except:
            raise Exception('Was not able to proceed with the flow')


class Footer:
    def __init__(self, driver):
        self.driver = driver

    def is_footer_displayed(self):
        """
        Method will check if element is displayed
        """
        return self.driver.find_element(*SauceWebFooterSelectors.FOOTER)


class BurgerMenuItems:
    def __init__(self, driver):
        self.driver = driver

    def click_burger_menu(self):
        """
        Method will click burger menu
        """
        try:
            self.driver.find_element(*SauceWebBurgerMenuSelectors.BURGER_MENU).click()
        except:
            raise Exception('Burger menu was not clicked')

    def logout_flow(self):
        """
        Method will complete logoutflow
        """
        try:
            self.click_burger_menu()
            self.driver.find_element(*SauceWebBurgerMenuSelectors.LOGOUT).click()
        except:
            raise Exception('Logout flow was not completed')

    def is_all_items_displayed(self):
        """
        Method will check if element is displayed
        """
        return self.driver.find_element(*SauceWebBurgerMenuSelectors.ALL_ITEMS)

    def is_about_displayed(self):
        """
        Method will check if element is displayed
        """
        return self.driver.find_element(*SauceWebBurgerMenuSelectors.ABOUT)

    def is_logout_displayed(self):
        """
        Method will check if element is displayed
        """
        return self.driver.find_element(*SauceWebBurgerMenuSelectors.LOGOUT)

    def is_reset_app_displayed(self):
        """
        Method will check if element is displayed
        """
        return self.driver.find_element(*SauceWebBurgerMenuSelectors.RESET_APP)

    def is_all_burger_menu_items_displayed(self):
        """
        This method checks for visibility of burger menu elements
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

    def is_added_item_displayed(self):
        """
        Method will check if element is displayed
        """
        if self.driver.find_element(*SauceWebPurcheseSelectors.REMOVE_CART).is_displayed():
            print('Added item presented')
        else:
            print('Added item not presented')


class BodyItems:
    def __init__(self, driver):
        self.driver = driver

    def is_first_item_displayed(self):
        """
        Method will check if element is displayed
        """
        if self.driver.find_element(*SauseWebBodyItemSelectors.FIRST_ITEM).is_displayed():
            print('Backpack presented')
        else:
            print('Backpack not presented')

    def is_second_item_displayed(self):
        """
        Method will check if element is displayed
        """
        if self.driver.find_element(*SauseWebBodyItemSelectors.SECOND_ITEM).is_displayed():
            print('Bike Light presented')
        else:
            print('Bike Light not presented')

    def is_third_item_displayed(self):
        """
        Method will check if element is displayed
        """
        if self.driver.find_element(*SauseWebBodyItemSelectors.THIRD_ITEM).is_displayed():
            print('Bolt T-Shirt presented')
        else:
            print('Bolt T-Shirt not presented')

    def is_forth_item_displayed(self):
        """
        Method will check if element is displayed
        """
        if self.driver.find_element(*SauseWebBodyItemSelectors.FORTH_ITEM).is_displayed():
            print('Jacket presented')
        else:
            print('Jacket not presented')

    def is_fifth_item_displayed(self):
        """
        Method will check if element is displayed
        """
        if self.driver.find_element(*SauseWebBodyItemSelectors.FIFTH_ITEM).is_displayed():
            print('Onesie presented')
        else:
            print('Onesie not presented')

    def is_sixth_item_displayed(self):
        """
        Method will check if element is displayed
        """
        if self.driver.find_element(*SauseWebBodyItemSelectors.SIXTH_ITEM).is_displayed():
            print('T-Shirt presented')
        else:
            print('T-Shirt not presented')

    def is_all_body_items_displayed(self):
        """
        This method checks for visibility of body elements
        :return: True or False
        """
        body_items = [self.is_fifth_item_displayed(), self.is_sixth_item_displayed(),
                      self.is_forth_item_displayed(), self.is_third_item_displayed(),
                      self.is_second_item_displayed(), self.is_first_item_displayed()]
        error_count = 0
        for method in body_items:
            if method is False:
                error_count += 1
        if error_count > 0:
            return False
        else:
            return True


class Logo:
    def __init__(self, driver):
        self.driver = driver

    def get_logo_text(self):
        """
        Method will get the text from an element
        """
        return self.driver.find_element(*SauseWebLogoSelectors.LOGO).text

    def check_logo_text(self):
        """
        Method will assert if actual and expected text are
        :return: True or False
        """
        if self.get_logo_text() == "Swag Labs":
            return True
        else:
            return False


class CategoriesMenu:
    def __init__(self, driver):
        self.driver = driver

    def categories_availability_z_a(self):
        """
        Method will verify if all items are displayed after categories are changed
        """
        expected_payment_methods = ['Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Onesie', 'Sauce Labs Fleece Jacket',
                                    'Sauce Labs Bolt T-Shirt', 'Sauce Labs Bike Light', 'Sauce Labs Backpack']
        available_payment_methods = self.driver.find_elements(*SauseWebBodyItemSelectors.INVENTORY_NAME)
        for items in available_payment_methods:
            print(items.text)
        if expected_payment_methods == available_payment_methods:
            return True
        else:
            return False

    def categories_availability_a_z(self):
        """
        Method will verify if all items are displayed after categories are changed
        """
        expected_payment_methods = ['Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Onesie', 'Sauce Labs Fleece Jacket',
                                    'Sauce Labs Bolt T-Shirt', 'Sauce Labs Bike Light', 'Sauce Labs Backpack']
        available_payment_methods = self.driver.find_elements(*SauseWebBodyItemSelectors.INVENTORY_NAME)
        for items in available_payment_methods:
            print(items.text)
        if expected_payment_methods == available_payment_methods:
            return True
        else:
            return False

    def categories_availability_high_low(self):
        """
        Method will verify if all items are displayed after categories are changed
        """
        expected_payment_methods = ['Sauce Labs Fleece Jacket', 'Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt',
                                    'Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Bike Light', 'Sauce Labs Onesie']
        available_payment_methods = self.driver.find_elements(*SauseWebBodyItemSelectors.INVENTORY_NAME)
        for items in available_payment_methods:
            print(items.text)
        if expected_payment_methods == available_payment_methods:
            return True
        else:
            return False

    def categories_availability_low_high(self):
        """
        Method will verify if all items are displayed after categories are changed
        """
        expected_payment_methods = ['Sauce Labs Onesie', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt',
                                    'Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Backpack', 'Sauce Labs Fleece Jacket']
        available_payment_methods = self.driver.find_elements(*SauseWebBodyItemSelectors.INVENTORY_NAME)
        for items in available_payment_methods:
            print(items.text)
        if expected_payment_methods == available_payment_methods:
            return True
        else:
            return False

    def click_categories_menu(self):
        """
        Method will click categories menu
        """
        try:
            self.driver.find_element(*SauceWebCategoriesSelectors.CATEGORIES).click()
        except:
            raise Exception ('Categories menu was not clicked')

    def click_categories_z_a_menu(self):
        """
        Method will click Z to A categories menu
        """
        try:
            select = Select(self.driver.find_element(*SauceWebCategoriesSelectors.CATEGORIES))
            select.select_by_value('za')
        except:
            raise Exception ('Categories Z to A was not clicked')

    def click_categories_high_low_menu(self):
        """
        Method will click High to Low categories menu
        """
        try:
            select = Select(self.driver.find_element(*SauceWebCategoriesSelectors.CATEGORIES))
            select.select_by_value('hilo')
        except:
            raise Exception ('Categories High to Low was not clicked')

    def click_categories_low_high_menu(self):
        """
        Method will click Low to High categories menu
        """
        try:
            select = Select(self.driver.find_element(*SauceWebCategoriesSelectors.CATEGORIES))
            select.select_by_value('lohi')
        except:
            raise Exception ('Categories Low to High was not clicked')
