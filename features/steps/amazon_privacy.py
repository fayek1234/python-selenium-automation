import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when,  then


PRIVACY_NOTICE = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")


@given("Open Amazon T&C  page")
def open_amazon_TC_page(context):
     context.driver.get(f'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when("Store original windows")
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original; window:', context.original_window)


@when("click on Amazon Privacy Notice link")
def amazon_privacy_notice_link(context):
     context.driver.find_element(*PRIVACY_NOTICE).click()
     time.sleep(2)



@when("Switch to new opened window")
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    time.sleep(2)
    print('Current windows:', context.driver.window_handles)
    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)


@then("verify user can see Amazon privacy Notice  page is Opened")
def verify_amazon_privacy_page_is_opened(context):
   context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display'))


@then("user can close new window")
def close_new_window(context):
    context.driver.close()


@then("go back to original window")
def original_window(context):
    context.driver.switch_to.window(context.original_window)
