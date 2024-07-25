from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page




class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH,"//h2[@data-test='resultsHeadingWithoutCount']")

    def verify_text(self):
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TXT).text
        assert 'rice cooker' in actual_text, f'Expected rice cooker not in actual {actual_text}'

    #def verify_url(self):
       # url = self.driver.current_url
      #  assert 'rice cooker' in url, f'Expected "rice cooker" not in {url}'