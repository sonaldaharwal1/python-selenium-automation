from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page




class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT =( By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")

    def click_add_to_cart(self):
        self.wait_and_click(*self.ADD_TO_CART_BTN )

    def store_product_name(self):
        self.product_name = self.driver.find_element(*self.SIDE_NAV_PRODUCT_NAME).text
        print(f'Product stored: {self.product_name}')

    def side_nav_click_add_to_cart(self):
     self.driver.find_element(*self.SIDE_NAV_ADD_TO_CART_BTN).click()


    def verify_search_results(self,expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TXT)

    def verify_product_in_url(self,expected_product):
        url = self.driver.current_url
        self.verify_partial_url(expected_product)