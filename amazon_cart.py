from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:/Users\khizi\Automation\python-selenium-automation\chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon ').click()
driver.find_element(By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty')

expected_text = "'your amazon cart is empty'"
actual_text = driver.find_element(By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty').text

assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'
print('Test case passed')
driver.quit()

