from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:/Users\khizi\Automation\python-selenium-automation\chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# By ID
driver.find_element(By.ID, 'nav-logo-sprites').Click('amazon logo')

# By XPATH attributes
driver.find_element(By.XPATH, "//input[@type='submit']")
# BY XPATH partial attributes
driver.find_element(By.XPATH, "//span[contains(text(), ' Need help?')]")
driver.find_element(By.XPATH, "//a[contains(@href, 'gp/help/customer/account-issue')]")
driver.find_element(By.XPATH, "//a[contains(text(), ' Create your Amazon account')]")