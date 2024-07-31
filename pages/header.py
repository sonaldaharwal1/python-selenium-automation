from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page



class Header(Page):
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")


    def search_product(self, product):
        print('POM layer:', product)
        self.input_text( product,   *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)

    sleep(6)

    def click_cart(self):
        self.wait_and_click(*self.CART_BTN)

    def click_sign_in(self):
        self.wait_and_click(*self.SIGN_IN_BTN)
