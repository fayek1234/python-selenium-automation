from pages.main_page import MainPage
from pages.header1 import Header
from pages.sign_in_page import SignInPage
from pages.empty_cart_page import EmptyCartPage




class Application:
    def __int__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.header1 = Header(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.empty_cart_page = EmptyCartPage(self.driver)




