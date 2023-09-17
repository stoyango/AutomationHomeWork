import unittest
import json
import csv
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
import os
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options



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
        # siteurl = "https://www.saucedemo.com/"
        screen_width = 2560
        screen_height = 1440
        output_directory = 'screenshots'
        sites = [""]
        options = Options()
        options.add_argument("--headless")
        os.makedirs(output_directory , exist_ok=True)
        for url in sites:
            print("get " + url + "...")
            filename = url.replace('/','_') + "logged_in_items.png"
            # cls.driver.get("https://www.saucedemo.com/" + url)
            sleep(3)
            outfile = os.path.join(output_directory, filename)
            cls.driver.get_screenshot_as_file(outfile)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
