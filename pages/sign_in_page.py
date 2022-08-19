from selenium.webdriver.common.by import By

from pages.base_page import Page




class SignInPage(Page):
    SIGN_IN = (By.XPATH, "//h1[@class='a-spacing-small']")
    VERIFY_EMAIL = (By.ID, 'ap_email')

    def verify_sign_in_page(self, expected_text):
        expected_text = 'Sign-In'
        actual_text = self.driver.find_element(*self.SIGN_IN).text
        assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'

        assert self.find_elements(*self.VERIFY_EMAIL)


