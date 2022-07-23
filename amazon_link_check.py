from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:/Users\khizi\Automation\python-selenium-automation\chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()
driver.find_element(By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a ')

expected_amount = int(expected_amount)  # '5' => 5
links = context.driver.find_elements(*FOOTER_LINKS)

assert len(links) == expected_amount, \
    f'Expected {expected_amount} links but got {len(links)}'