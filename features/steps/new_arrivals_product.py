from selenium.webdriver.common.by import By
from behave import given, when, then


# @given('Open Amazon product {product_id} page')
# def open_amazon_product(context, product_id):
#     context.app.amazon_product_pag.open_amazon_product(product_id)


@given("Open the Amazon Product Page for {product_id}")
def step_impl(context, product_id):
    context.app.amazon_product_page.open_amazon_product(product_id)



@then('hover over to new arrivals')
def hover_over_new_arrivals(context):
    context.app.hover_over_page.hover_over_new_arrivals()


@then('verify user can see new arrivals deals')
def verify_new_arrivals_deals(context):
    context.app.more_products_page.verify_new_arrivals_deals()


