from selenium.webdriver.common.by import By

from pages.base_page import Page


class TermsAndConditions(Page):

    def verify_Terms_and_Conditions_opened_url(self):
        self.verify_partial_url('/terms-condition')