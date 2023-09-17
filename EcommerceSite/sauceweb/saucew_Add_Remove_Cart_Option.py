#
# import unittest
# from selenium import webdriver
# from EcommerceSite.sauceweb.Specific.page import MainPage
# # import page
#
# class PythonOrgSearch(unittest.TestCase):
#     """A sample test class to show how page object works"""
#
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.get("http://www.python.org")
#
#     def test_search_in_python_org(self):
#         """Tests python.org search feature. Searches for the word "pycon" then
#         verified that some results show up.  Note that it does not look for
#         any particular text in search results page. This test verifies that
#         the results were not empty."""
#
#         #Load the main page. In this case the home page of Python.org.
#         main_page = MainPage(self.driver)
#         #Checks if the word "Python" is in title
#         self.assertTrue(main_page.is_title_matches(), "python.org title doesn't match.")
#         #Sets the text of search textbox to "pycon"
#         main_page.search_text_element = "pycon"
#         main_page.click_go_button()
#         search_results_page = page.SearchResultsPage(self.driver)
#         #Verifies that the results page is not empty
#         self.assertTrue(search_results_page.is_results_found(), "No results found.")
#
#     # def tearDown(self):
#     #     self.driver.close()
#
# # if __name__ == "__main__":
# #     unittest.main()

import unittest
import json
from selenium import webdriver
from EcommerceSite.sauceweb.Specific.sauce_login_page import LoginPage
from EcommerceSite.sauceweb.Specific.sauce_logged_in_page import LoggedInPage
from EcommerceSite.sauceweb.Specific.sauce_login_page_selectors import SauceWebLoginPageSelectors
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from BasePage.credentials import drivers_config



class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.saucedemo.com/")
        cls.driver.get(drivers_config["URL"])
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

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
