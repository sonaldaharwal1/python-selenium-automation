from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
@when('Open cart page')
def open_cart(context):
    context.app.cart_page.open_cart()


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.cart_page.verify_product_name()

@then('Verify cart has {amount} item(s)')
def verify_cart_items(context,amount):
    context.app.cart_page.verify_cart_items(amount)


@then('Verify “Your cart is empty” message is shown')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()

