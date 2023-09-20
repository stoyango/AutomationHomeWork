import unittest
import json
from selenium import webdriver
from EcommerceSite.sauceweb.Specific.sauce_login_page import LoginPage
from EcommerceSite.sauceweb.Specific.sauce_logged_in_page import LoggedInPage
# from EcommerceSite.sauceweb.Specific.sauce_login_page_selectors import SauceWebLoginPageSelectors
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from BasePage.credentials import drivers_config



class LoginTest(unittest.TestCase):
    logged_in = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.saucedemo.com/")
        # cls.driver.get(drivers_config["URL"])
        cls.driver.maximize_window()


    def test_01_login(self):
        try:
            login = LoginPage(self.driver)
            login.is_login_modal_displayed()
            login.login_flow("standard_user", "secret_sauce")
            logged_in = LoggedInPage(self.driver)
            logged_in.is_header_logged_displayed()
        except:
            raise Exception ('was no able to complete login flow')

    def test_02_body_items(self):
        try:
            logged_in = LoggedInPage(self.driver)
            logged_in.is_all_body_items_displayed()
        except:
            raise Exception ('was no able to complete login flow')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
