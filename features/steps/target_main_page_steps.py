from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.app.main_page.open()

@given('Open target circle page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')

@when('Search for {product}')
def search_product(context, product):
    context.app.header.search()
    sleep(6)


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()

