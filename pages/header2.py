from selenium.webdriver.common.by import By

from pages.base_page import Page

class Header(Page):
    CLICK_CART = (By.CSS_SELECTOR, 'span.nav-cart-icon ')

    def click_cart(self,):
        self.click(*self. CLICK_CART)
        self.click()