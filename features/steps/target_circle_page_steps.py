from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@then('Verify page has {number} links')
def verify_header_link_amount(context, number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[class='sc-fb3945a7-5 fBbzFg']")
    assert len(links) == number, f'Expected {number} links but got {len(links)}'


@then('Verify can click every link')
def verify_click_links(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")

    for i in range(len(links)):
        # Search for links again because their internal IDs changed:
        # to avoid Stale Element Exception
        links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
        print(f'Clicking on link {links[i].text}')
        links[i].click()
        sleep(4)