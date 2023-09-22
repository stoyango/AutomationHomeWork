import unittest
from selenium import webdriver
from EcommerceSite.sauceweb.Specific.sauce_login_page import LoginPage
from EcommerceSite.sauceweb.Specific.sauce_logged_in_page import LoggedInPage, BodyItems



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
            logged_in = LoggedInPage(self.driver)
            logged_in.is_header_logged_displayed()
        except:
            raise Exception ('Was no able to complete login flow')

    def test_02_body_items(self):
        try:
            body_items = BodyItems(self.driver)
            body_items.is_all_body_items_displayed()
        except:
            raise Exception ('Was no able to verify body items')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
