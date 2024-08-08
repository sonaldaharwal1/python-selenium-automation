from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



@given('Open sign in page')
def open_target_login(context):
    context.app.sign_in_page.open_target_login()

@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()

sleep(4)
@when('Click on Target terms and conditions link')
def click_Terms_and_Conditions_link(context):
    context.app.sign_in_page.click_Terms_and_Conditions_link()

@when('Switch to the newly opened window')
def switch_window(context):
    context.app.sign_in_page.switch_to_new_window()

@then('Verify Terms and Conditions page is opened')
def verify_Terms_and_Conditions_opened(context):
    context.app.terms_and_conditions_page.verify_Terms_and_Conditions_opened_url()

@then('Close current page')
def close(context):
    context.app.terms_and_conditions_page.close()

@then('Return to original window')
def return_to_original_window(context):
    context.app.terms_and_conditions_page.switch_to_window_by_id(context.original_window)





@then('Verify Sign In form opened')
def verify_sign_in_Page(context):
    context.app.sign_in_page.verify_sign_in_Page()

    sleep(4)