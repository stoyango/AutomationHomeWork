from selenium.webdriver.common.by import By
from EcommerceSite.sauceweb.Specific.sauce_logged_in_page_selectors import SauceWebPurcheseSelectors, \
    SauceWebBurgerMenuSelectors, SauceWebLoggedIn, SauceWebLogOutSelectors, SauceWebFooterSelectors
from BasePage.base_page import BasePage

class LoggedInPage():
    def __init__(self, driver):
        self.driver = driver


    def is_header_logged_displayed(self):
        if self.driver.find_element(*SauceWebLoggedIn.HEADER_CONTAINER).is_displayed():
            print('header presented')
        else:
            print('header not presented')

    def purchase_item_flow(self, username, password, zipcode):
        try:
            self.driver.find_element(*SauceWebPurcheseSelectors.ADD_CART).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.SHOPPING_CART).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.CHECKOUT).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.FIRST_NAME).send_keys(username)
            self.driver.find_element(*SauceWebPurcheseSelectors.LAST_NAME).send_keys(password)
            self.driver.find_element(*SauceWebPurcheseSelectors.POST_CODE).send_keys(password)
            self.driver.find_element(*SauceWebPurcheseSelectors.CONTINUE).click()
            self.driver.find_element(*SauceWebPurcheseSelectors.FINISH).click()
            if self.driver.find_element(*SauceWebPurcheseSelectors.COMLETE).is_displayed():
                print('complete presented')
            else:
                print('complete not presented')
        except:
            raise Exception ('')

    def logout_flow(self):
        try:
            self.click_burger_menu()
            self.driver.find_element(*SauceWebLogOutSelectors.LOG_OUT).click()
        except:
            raise Exception ('')

    def click_burger_menu(self):
        try:
            self.driver.find_element(*SauceWebBurgerMenuSelectors.BURGER_MENU).click()
        except:
            raise Exception ('')

    def is_footer_displayed(self):
        if self.driver.find_element(*SauceWebFooterSelectors.FOOTER).is_displayed():
            print('footer presented')
        else:
            print('footer not presented')


    def test_search_in_python_org(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""
        self.assertTrue(main_page.is_title_matches(), "python.org title doesn't match.")
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        self.assertTrue(search_results_page.is_results_found(), "No results found.")




