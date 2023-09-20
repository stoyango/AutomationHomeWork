import unittest
from selenium import webdriver
from EcommerceSite.sauceweb.Specific.sauce_login_page import LoginPage
from EcommerceSite.sauceweb.Specific.sauce_logged_in_page import LoggedInPage
# from EcommerceSite.sauceweb.Specific.sauce_login_page_selectors import SauceWebLoginSelectors, SauceWebLogOutSelectors
from selenium.webdriver.common.by import By
# from selenium.

class LoginTest(unittest.TestCase):
    logged_in = None

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
            self.__class__.logged_in = LoggedInPage(self.driver)
            self.__class__.logged_in.is_header_logged_displayed()
        except:
            raise Exception ('was no able to complete login flow')

    def test_02_purchase_flow(self):
        try:
           self.__class__.logged_in.add_cart_flow()
           self.__class__.logged_in.remove_cart_flow()
        except:
            raise Exception ('was no able to complete login flow')

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
