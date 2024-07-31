from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_MSG = (By.ID, 'login')

    def verify_sign_in_Page(self):
        self.wait_for_element_appear(*self. SIGN_IN_MSG)
        self.verify_text('Sign in with password', *self.SIGN_IN_MSG)