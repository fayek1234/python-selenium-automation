from selenium.webdriver.common.by import By
from behave import given, when, then


@when('user click on order')
def click_order(context):
    context.driver.find_element(By.XPATH, "//span[text()='Returns']").click()




@then('user see result')
def verify_search_result(context):
    expected_text = 'Sign-In'
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'

@then('user can search for email')
def search_for_email(context):
        context.driver.find_element(By.ID, 'ap_email')