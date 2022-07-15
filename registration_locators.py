from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:/Users\khizi\Automation\python-selenium-automation\chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# By Class
driver.find_element(By.CSS_SELECTOR, 'i.a-icon-logo')
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# By CSS, ID
driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name')
driver.find_element(By.CSS_SELECTOR, 'input#ap_email')
driver.find_element(By.CSS_SELECTOR, 'input#ap_password_check')
driver.find_element(By.CSS_SELECTOR, 'input#continue')
# By XPATH
driver.find_element(By.XPATH, "//input[@name='password']")
# By CSS, attributes
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")



