from selenium.webdriver.support import expected_conditions as ec

class BasePage():
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)


    def find_elements(self, *selector):
        return self.driver.find_element(*selector)

    def find_element(self, *selector):
        """
        This method returns an element
        based on provided selector
        :param selector: set selector
        :return: element
        """
        return self.driver.find_element(*selector)

    def scroll_to_all_games_btn(self):
        self.scroll_to_element(*GamesSectionSelectors.ALL_GAMES_BTN)

    def scroll_to_element(self, *selector):
        """
        This method performs scrolling to
        specified element
        :param selector: set selector
        """
        element = self.find_element(*selector)
        scroll = ActionChains(self.driver).move_to_element(element)
        scroll.perform()

    def click_on_element(self, element_name, selector):
        try:
            self.cliable_element(selector=selector).click()
        except:
            raise Exception('asd')

    def visibility_of_element(self, selector):
        return self.wait.until(ec.visibility_of_element_located(selector))

    # def is_element_displayed(self, element_name, selector):
    #     """
    #     This method checks if an element
    #     is displayed or not
    #     :param element_name: set string name of the element
    #     :param selector: set selector
    #     :return: True or False
    #     """
    #     try:
    #         self.driver.find_element(selector=selector)
    #         print(f"--> {element_name} is displayed.")
    #     except TimeoutException:
    #         print(f"### {element_name} is not displayed! " + str(selector))
    #         return False
    #     return True


