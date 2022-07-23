import time

from selenium.webdriver.common.by import By
from behave import given, when,  then

INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
ADD_TO_CART_BTN = (By. ID, 'add-to-cart-button')
CART = (By. ID, 'nav-cart-count')


@given(' Open Amazon page ')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == actual_text, f'Expected {expected_count}  but got {actual_text}'


@when("search for {search_word}")
def step_impl(context, search_word):
    context.driver.find_element(*INPUT_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_ICON).click()


@when("Click on the first product")
def step_impl(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@when("Click on Add to cart button")
def step_impl(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when("Open cart page")
def step_impl(context):
    time.sleep(3)
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')