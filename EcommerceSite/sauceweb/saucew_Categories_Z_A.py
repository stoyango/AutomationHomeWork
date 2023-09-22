import unittest
from selenium import webdriver
from EcommerceSite.sauceweb.Specific.sauce_login_page import LoginPage
from EcommerceSite.sauceweb.Specific.sauce_logged_in_page import LoggedInPage, CategoriesMenu


class LoginTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.saucedemo.com/")
        cls.driver.maximize_window()

    def test_01_categories_z_a(self):
        try:
            login = LoginPage(self.driver)
            login.is_login_modal_displayed()
            login.login_flow("standard_user", "secret_sauce")
            logged_in = LoggedInPage(self.driver)
            logged_in.is_header_logged_displayed()
            categories = CategoriesMenu(self.driver)
            categories.click_categories_menu()
            categories.click_categories_z_a_menu()
            categories.categories_availability_z_a()
            print('Z to A categories were verified successfully')
        except:
            raise Exception('Z to A categories were not verified')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
