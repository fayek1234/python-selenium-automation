from selenium.webdriver.common.by import By

from pages.base_page import Page

class Result_Page(Page):

   NAV_SUBNAV = (By.CSS_SELECTOR, "#nav-subnav[data-category='pc']")

   def verify_computers_department(self):
        self.wait_for_element_appear(*self. NAV_SUBNAV)









