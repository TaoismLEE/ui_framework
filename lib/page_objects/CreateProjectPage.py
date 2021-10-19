# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from lib.page_objects.BasePage import BasePage


class CreateProjectPage(BasePage):
    """
    create project page, each page can be maintain as a class inheriting from BasePage
    Locators: maintain elements locators of current page
    Functions: maintain functions can perform on current page
    """

    # Locators
    loc_dialog_env = (By.XPATH, "//input[contains(@placeholder, 'User Name')]")

    # Functions
    def input_user_name(self, name):
        self.find_element(*self.loc_dialog_env)