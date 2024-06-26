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
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# find amazon logo by xpath
driver.find_element(By.XPATH,("//i[@class='a-icon a-icon-logo']"))

# find Email field by ID
driver.find_element(By.ID,'ap_email')

# find Continue button by ID
driver.find_element(By.ID,'continue')

# find Conditions of use link by Xpath
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Conditions of Use']")

# find Privacy Notice link by Xpath
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Privacy Notice']")

# find Need help link by Xpath
driver.find_element(By.XPATH,("//span[@class='a-expander-prompt']"))

# find Forgot your password link by ID
driver.find_element(By.ID,'auth-fpp-link-bottom')

# find Other issues with Sign-In link by ID
driver.find_element(By.ID,'ap-other-signin-issues-link')

#find Create your Amazon account button by ID
driver.find_element(By.ID,'createAccountSubmit')
sleep(5)
