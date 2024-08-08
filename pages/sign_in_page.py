from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_MSG = (By.ID, 'login')
    TERMS_AND_CONDITIONS_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")

    def open_target_login(self):
        self.open_url(' https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')




    def click_Terms_and_Conditions_link(self):
        self.click(*self.TERMS_AND_CONDITIONS_LINK)

        sleep(5)

    def verify_sign_in_Page(self):
        self.wait_for_element_appear(*self. SIGN_IN_MSG)
        self.verify_text('Sign in with password', *self.SIGN_IN_MSG)