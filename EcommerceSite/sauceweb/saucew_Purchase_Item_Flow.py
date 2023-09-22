import unittest
from selenium import webdriver
from EcommerceSite.sauceweb.Specific.sauce_login_page import LoginPage
from EcommerceSite.sauceweb.Specific.sauce_logged_in_page import LoggedInPage


class PurchaseItemFlow(unittest.TestCase):
    logged_in = None
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.saucedemo.com/")
        cls.driver.maximize_window()

    def test_01_purchase_flow(self):
        try:
            login = LoginPage(self.driver)
            login.is_login_modal_displayed()
            login.login_flow("standard_user", "secret_sauce")
            logged_in = LoggedInPage(self.driver)
            logged_in.is_header_logged_displayed()
            logged_in.purchase_item_flow("Stoyan","G","1505")
        except:
            raise Exception ('Was no able to complete purchase flow')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
