from EcommerceSite.sauceweb.Specific.sauce_login_page_selectors import SauceWebLoginPageSelectors


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def is_login_modal_displayed(self):
        """
        Method will check if element is displayed
        """
        if self.driver.find_element(*SauceWebLoginPageSelectors.LOGIN_BTN).is_displayed():
            print('Login modal is presented')
        else:
            print('Login modal not presented')

    def is_error_msg_displayed(self):
        """
        Method will check if element is displayed
        """
        if self.driver.find_element(*SauceWebLoginPageSelectors.ERROR_MSG).is_displayed():
            print('Error msg presented')
        else:
            print('Error msg not presented')

    def login_flow(self, username, password):
        """
        Method will complete login flow
        """
        try:
            self.driver.find_element(*SauceWebLoginPageSelectors.LOGIN_USERNAME_FIELD).send_keys(username)
            self.driver.find_element(*SauceWebLoginPageSelectors.LOGIN_PASSWORD_FIELD).send_keys(password)
            self.driver.find_element(*SauceWebLoginPageSelectors.LOGIN_BTN).click()
            print('Login flow was completed')
        except:
            raise Exception('Could not complete login flow')
