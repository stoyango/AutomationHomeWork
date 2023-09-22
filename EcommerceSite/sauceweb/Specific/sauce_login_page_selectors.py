from selenium.webdriver.common.by import By

"""
Selectors for Sauce Web login form
"""

class SauceWebLoginPageSelectors(object):
    LOGIN_BTN = (By.ID, "login-button")
    LOGIN_USERNAME_FIELD = (By.ID, "user-name")
    LOGIN_PASSWORD_FIELD = (By.ID, "password")
    ERROR_MSG = (By.CSS_SELECTOR, ".error-message-container")



