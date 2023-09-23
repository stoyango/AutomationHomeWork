import unittest
from selenium import webdriver
from EcommerceSite.sauceweb.Specific.sauce_login_page import LoginPage
from EcommerceSite.sauceweb.Specific.sauce_logged_in_page import LoggedInPage, BodyItems


class LoginTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.saucedemo.com/")
        cls.driver.maximize_window()

    def test_01_login(self):
        try:
            login = LoginPage(self.driver)
            login.is_login_modal_displayed()
            login.login_flow("standard_user", "secret_sauce")
            logged_in = LoggedInPage(self.driver)
            logged_in.is_header_logged_displayed()
        except:
            raise Exception('Was no able to complete login flow')

    def test_02_items_check(self):
        try:
            items = BodyItems(self.driver)
            items.click_backpack_item()
            self.assertTrue(items.check_backpack_text,
                            "Sauce Labs Backpack text dont match")
            print('Sauce Labs Backpack was displayed')
            items.click_back_navigation()
            items.click_bike_light_item()
            self.assertTrue(items.check_bike_light_text(),
                            "Sauce Labs Bolt T-Shirt Text dont match")
            print('Sauce Labs Bolt T-Shirt was displayed')
            items.click_back_navigation()
            items.click_bolt_tshirt_item()
            self.assertTrue(items.check_bolt_tshirt_text(),
                            "Sauce Labs Bike Light Text dont match")
            print('Sauce Labs Bike Light was displayed')
            items.click_back_navigation()
            items.click_fleece_jacket_item()
            self.assertTrue(items.check_fleece_jacket_text(),
                            "Sauce Labs Fleece Jacket Text dont match")
            print('Sauce Labs Fleece Jacket was displayed')
            items.click_back_navigation()
            items.click_onesie_item()
            self.assertTrue(items.check_onesie_text(),
                            "Sauce Labs Onesie Text dont match")
            print('Sauce Labs Onesie was displayed')
            items.click_back_navigation()
            items.click_red_tshirt_item()
            self.assertTrue(items.check_red_tshirt_text(),
                            "Test.allTheThings() T-Shirt (Red) Text dont match")
            print('Test.allTheThings() T-Shirt (Red) was displayed')
            items.click_back_navigation()
        except:
            raise Exception('Was no able to complete items validation flow')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
