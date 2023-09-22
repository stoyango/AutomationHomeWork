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

    def test_01_burger_menu(self):
        try:
            login = LoginPage(self.driver)
            login.is_login_modal_displayed()
            login.login_flow("standard_user", "secret_sauce")
            logged_in = LoggedInPage(self.driver)
            logged_in.is_header_logged_displayed()
            burger_menu = BurgerMenuItems(self.driver)
            burger_menu.click_burger_menu()
            burger_menu.is_all_burger_menu_items_displayed()
            print('Burger Menu items were verified successfully')
        except:
            raise Exception ('Could not verify burger menu items')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
