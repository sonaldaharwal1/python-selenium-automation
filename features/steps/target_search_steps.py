from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@when('Add {product} into cart')
def add_product(context, product):
    # find product and click add to cart
    context.driver.find_element(By.ID,'addToCartButtonOrTextIdFor14072552').click()

@when('Chose option and add {product}into cart')
def search_product(context, product):

    context.driver.find_element(By.XPATH, "//button[@data-test='orderPickupButton']").click()



@when('Click on view cart & check out')
def click_view_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class='sc-9306beff-0 sc-e6042511-0 dfqbQr ibmrHV']").click()

    sleep(6)
@then('Verify search results shown for {product}')
def verify_search_results(context, product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_text, f'Expected {product} not in actual {actual_text}'












