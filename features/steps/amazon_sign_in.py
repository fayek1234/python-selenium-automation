from selenium.webdriver.common.by import By
from behave import given, when, then


@when('user click on order')
def click_order(context):
   #context.driver.find_element(By.CSS_SELECTOR, "a[href='/gp/css/order-history?ref_=nav_orders_first']").click()
   context.app.header1.click_order()




@then('user see result')
def verify_search_result(context):
    context.app.sign_in_page.verify_sign_in_page()
    #expected_text = 'Sign-In
    #actual_text = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
   #assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'

#@then('user can search for email')
#def search_for_email(context):
       # context.driver.find_element(By.ID, 'ap_email')