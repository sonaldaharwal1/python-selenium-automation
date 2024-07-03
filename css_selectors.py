from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# Find amazon logo by css:
# using attributes:
driver.find_element(By.CSS_SELECTOR, "[aria-label='Amazon']")

#Find create account by css using, tag + classes
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# Find your name tab by css, using id:
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# Find Email by css, using id:
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# Find password tab by css, using id:
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# Find Passwords must be at least 6 characters.by css, using id:
driver.find_element(By.CSS_SELECTOR, "#auth-password-missing-alert")

# Find Re-enter password tab by css, using tag, id and attributes:
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check[type='password']")

# Find  create your amazon account by css, using tag and  id:
driver.find_element(By.CSS_SELECTOR, "input#continue")

# Find condition to use using, Attributes, partial match
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

# Find privacy notice using, Attributes, partial match
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

# Find Sign tab by css ,using tag + classes
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis")


sleep(5)