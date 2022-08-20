from selenium.webdriver.common.by import By

from pages.base_page import Page

class More_Products(Page):

    MORE_PRODUCTS = (By.CSS_SELECTOR, "img[src='https://m.media-amazon.com/images/G/01//AMAZON_FASHION/2022/SITE_FLIPS/SPR_22/SUBNAV/M._CB1648157817_.jpg']")

    def verify_new_arrivals_deals(self):
        self.click(*self.MORE_PRODUCTS)
        self.click()
        