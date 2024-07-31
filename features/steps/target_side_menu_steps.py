from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



@when('From right side menu & click Sign In')
def click_side_sign_in(context):
    context.app.side_menu_page.click_side_sign_in()