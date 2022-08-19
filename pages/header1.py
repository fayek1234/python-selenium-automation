from selenium.webdriver.common.by import By

from pages.base_page import Page

class Header(Page):
    CLICK_ORDER = (By.CSS_SELECTOR, "a[href='/gp/css/order-history?ref_=nav_orders_first']")

    def click_order(self,):
        self.click(*self.CLICK_ORDER).click()



