from selenium.webdriver.common.by import By

from pages.base_page import Page



class EmptyCartPage(Page):
    EMPTY_CART = (By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty')

    def verify_empty_cart(self, expected_text):
        actual_text = self.driver.find_element(*self.EMPTY_CART).text
        assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'