from selenium.webdriver.common.by import By
from pages.base_page import Page


class SideMenuPage(Page):
    SIDE_SIGN_BTN = (By.ID,'listaccountNav-signIn')


    def click_side_sign_in(self):
        self.wait_and_click(*self.SIDE_SIGN_BTN )