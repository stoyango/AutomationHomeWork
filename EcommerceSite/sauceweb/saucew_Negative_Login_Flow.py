import unittest
from selenium import webdriver
from EcommerceSite.sauceweb.Specific.sauce_login_page import LoginPage
from selenium.webdriver.common.by import By

class PurchaseItemFlow(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.saucedemo.com/")
        cls.driver.maximize_window()

    def test_01_login(self):
        try:
            login = LoginPage(self.driver)
            login.is_login_modal_displayed()
            login.login_flow("standard_userr", "secret_saucee")
            login.is_error_msg_displayed()
        except:
            raise Exception ('was no able to complete login flow')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
