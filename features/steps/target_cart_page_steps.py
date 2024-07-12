from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@then('Verify cart result shown for {product}')
def verify_cart_results(context, product):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[class='h-text-md h-text-grayDark h-margin-r-x2']").text
    assert product in actual_text, f'Expected {product} not in actual {actual_text}'



@then('Verify “Your cart is empty” message is shown')
def verify_cart_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg']").text
    assert expected_text in actual_text, f'Expected {expected_text} ot in actual {actual_text}'

