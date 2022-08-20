from selenium.webdriver.common.by import By

from pages.base_page import Page
from selenium.webdriver.support.ui import Select

class Header(Page):
    DEPARTMENT_SELECT = (By.ID, "searchDropdownBox")
    INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')

    def select_department(self,):
        department = self.find_element(*self.DEPARTMENT_SELECT)
        select = Select(department)
        select.select_by_value("search-alias=computers")


    def search_product(self, search_word):
       self.input_text(search_word, *self.INPUT_FIELD)
       self.click(*self.SEARCH_ICON)