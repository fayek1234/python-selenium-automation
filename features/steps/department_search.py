from selenium.webdriver.common.by import By
from behave import given, when, then




@when("select department computers")
def select_department(context):
    context.app.headerthree.select_department()


@when('Input {search_word} into search field')
def input_search(context, search_word):
    context.app.headerthree.search_product(search_word)


@then("verify computers department is selected")
def verify_computers_department(context):
    context.app.result_page.verify_computers_department()



