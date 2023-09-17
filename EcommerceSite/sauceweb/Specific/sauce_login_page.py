from selenium.webdriver.common.by import By
from EcommerceSite.sauceweb.Specific.sauce_login_page_selectors import SauceWebLoginPageSelectors
from BasePage.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

class LoginPage():
    def __init__(self, driver):
        self.driver = driver


    def is_login_modal_displayed(self):
        if self.driver.find_element(*SauceWebLoginPageSelectors.LOGIN_BTN).is_displayed():
            print('login presented')
        else:
            print('login not presented')

    def is_error_msg_displayed(self):
        if self.driver.find_element(*SauceWebLoginPageSelectors.ERROR_MSG).is_displayed():
            print('Error msg presented')
        else:
            print('Error msg not presented')

    def login_flow(self, username, password):
        try:
            self.driver.find_element(*SauceWebLoginPageSelectors.LOGIN_USERNAME_FIELD).send_keys(username)
            self.driver.find_element(*SauceWebLoginPageSelectors.LOGIN_PASSWORD_FIELD).send_keys(password)
            self.driver.find_element(*SauceWebLoginPageSelectors.LOGIN_BTN).click()
        except:
            raise Exception ('')
