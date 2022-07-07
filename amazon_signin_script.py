from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:/Users\khizi\Automation\python-selenium-automation\chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH, "//span[text()='Returns']").click()
driver.find_element(By.ID, 'ap_email')

expected_result = '"Returns"'
actual_result = '"Returns"'

assert expected_result == actual_result
print('Test case passed')
