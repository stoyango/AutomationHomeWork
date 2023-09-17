import unittest
from selenium import webdriver
from EcommerceSite.sauceweb.Specific.sauce_login_page import LoginPage
from EcommerceSite.sauceweb.Specific.sauce_logged_in_page import LoggedInPage
# from EcommerceSite.sauceweb.Specific.sauce_login_page_selectors import SauceWebLoginSelectors
# from EcommerceSite.sauceweb.Specific.sauce_logged_in_page_selectors import SauceWebScrollFooter
from EcommerceSite.sauceweb.Specific.sauce_logged_in_page import LoggedInPage
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.saucedemo.com/")
        login = LoginPage(cls.driver)
        login.is_login_modal_displayed()
        login.login_flow("standard_user", "secret_sauce")
        cls.driver.execute_script("window.scrollBy(0, document.documentElement.scrollHeight)")
        cls.driver.maximize_window()


    def test_01_login(self):
        try:
            logged_in = LoggedInPage(self.driver)
            logged_in.is_header_logged_displayed()
            logged_in.is_footer_displayed()
        except:
            raise Exception ('was no able to complete login flow')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
