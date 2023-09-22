import unittest
from selenium import webdriver
from EcommerceSite.sauceweb.Specific.sauce_login_page import LoginPage
from EcommerceSite.sauceweb.Specific.sauce_logged_in_page import LoggedInPage

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
            print('User logged in successfully')
        except:
            raise Exception ('Was no able to complete login flow')

    def test_02_add_remove_flow(self):
        try:
           self.__class__.logged_in.add_cart_flow()
           self.__class__.logged_in.remove_cart_flow()
           print('Add/Remove flow was successful')
        except:
            raise Exception ('Was no able to complete Add/Remove flow')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
