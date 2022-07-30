import time

from selenium.webdriver.common.by import By
from behave import given, when, then

COLOR_OPTIONS = (By. CSS_SELECTOR, "#color_name")
PRESENT_COLOR = (By. CSS_SELECTOR, "#variation_color_name .selection")

@given("Open Amazon product {product_id} page")
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')

@then("verify that user can go through colors")
def verify_can_click_colors(context):
    expected_colors = ['BLACK', 'Light Wash',  'Blue, Over Due',  'Bright White', 'Dark blue vintage', 'Dark Indigo',]

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    actual_colors = []


    for color in colors[:6]:
        color.click()
        actual_colors += [context.driver.find_element(*PRESENT_COLOR).text]
        print('Actual colors:', actual_colors)

        assert expected_colors[:6] == actual_colors, f'Expected {expected_colors} but got {actual_colors}'






