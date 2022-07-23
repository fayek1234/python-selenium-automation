import time

from selenium.webdriver.common.by import By
from behave import given, when, then




@when(' user click on best seller page ')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()


@then(' Verify {expected_amount} links ')
def verify_links(context, expected_amount):
    expected_amount = int(expected_amount)  # '5'
    links = context.driver.find_elements(By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a ')
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'


@when("user click on best seller page")
def click_cart(context):
    time.sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()


@then("verify {expected_amount} links")
def verify_links(context, expected_amount):
    expected_amount = int(expected_amount)  # '5'
    links = context.driver.find_elements(By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a ')
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'