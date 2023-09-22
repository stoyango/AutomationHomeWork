import unittest
from selenium import webdriver
from EcommerceSite.sauceweb.Specific.sauce_login_page import LoginPage


class PurchaseItemFlow(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.saucedemo.com/")
        cls.driver.maximize_window()

    def test_01_negative_login(self):
        try:
            login = LoginPage(self.driver)
            login.is_login_modal_displayed()
            login.login_flow("standard_userr", "secret_saucee")
            login.is_error_msg_displayed()
            print('Error msg was displayed')
        except:
            raise Exception ('Was no able to complete logout flow')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
