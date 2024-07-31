from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage (Page):
    CART_EMPTY_MSG=(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg']")
    CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def open_cart(self):
        self.open_url('https://www.target.com/cart')

    def verify_product_name(self):
        actual_name = self.driver.find_element(*self.CART_ITEM_TITLE).text
        print(f'Actual product in cart name: {actual_name}')
       # assert self.product_name in actual_name, f"Expected {self.product_name} but got {actual_name}"

    def verify_cart_items(self,amount):
        cart_summary = self.driver.find_element(*self.CART_SUMMARY).text
        assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"


    def verify_cart_empty(self):
        self.wait_for_element_appear(*self.CART_EMPTY_MSG)
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)