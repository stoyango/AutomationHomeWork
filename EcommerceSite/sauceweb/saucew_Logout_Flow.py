import unittest
from selenium import webdriver
from EcommerceSite.sauceweb.Specific.sauce_login_page import LoginPage
from EcommerceSite.sauceweb.Specific.sauce_logged_in_page import LoggedInPage, BurgerMenuItems


class LoginTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.saucedemo.com/")
        cls.driver.maximize_window()

    def test_01_logout(self):
        try:
            login = LoginPage(self.driver)
            login.is_login_modal_displayed()
            login.login_flow("standard_user", "secret_sauce")
            logged_in = LoggedInPage(self.driver)
            logged_in.is_header_logged_displayed()
            burger_menu = BurgerMenuItems(self.driver)
            burger_menu.logout_flow()
            login.is_login_modal_displayed()
        except:
            raise Exception ('was no able to complete login flow')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
