# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from lib.page_objects.BasePage import BasePage


class PageTemplate(BasePage):
    """
    Template, each page can be maintain as a class inheriting from BasePage
    Locators: maintain elements locators of current page
    Functions: maintain functions can perform on current page
    """

    # Locators
    # loc_name_input = (By.XPATH, "//input[contains(@placeholder, 'User Name')]")
    # loc_password_input = (By.CSS_SELECTOR, "xxxxx")

    # Functions
    # def input_user_name(self, name):
    #     self.find_element(*self.loc_name_input).send_keys(name)
    #
    # def input_password(self, password):
    #     self.find_element(*self.loc_password_input).send_keys(password)
