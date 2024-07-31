from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.app.search_results_page.click_add_to_cart()

@when('Store product name')
def store_product_name(context):
    context.app.search_results_page.store_product_name()


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.app.search_results_page.side_nav_click_add_to_cart()
    sleep(6)



@then('Verify search results shown for {expected_product}')
def verify_search_results(context,expected_product):
    context.app.search_results_page.verify_search_results(expected_product)

@then('Verify correct search results URL opens for {expected_product}')
def verify_url(context, expected_product):
    context.app.search_results_page.verify_product_in_url(expected_product)
    sleep(6)













