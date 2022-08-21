from selenium.webdriver.common.by import By

from pages.base_page import Page
from selenium.webdriver import ActionChains

class Hover_Over_Page(Page):

  NEW_ARRIVALS = (By. CSS_SELECTOR,  "a[href='/New-Arrivals/b/?_encoding=UTF8&node=17020138011&ref_=sv_sl_6']")


  def hover_over_new_arrivals(self):
      new_arrivals = self.find_element(*self.NEW_ARRIVALS)
      actions = ActionChains(self.driver)
      actions.move_to_element(new_arrivals)
      actions.perform()

