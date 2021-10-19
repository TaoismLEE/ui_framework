# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from lib.page_objects.BasePage import BasePage


class LoginPage(BasePage):
    """
    Home page of project, each page can be maintain as a class inheriting from BasePage
    Locators: maintain elements locators of current page
    Functions: maintain functions can perform on current page
    """

    # Locators
    loc_name_input = (By.XPATH, "//input[contains(@placeholder, 'User Name')]")
    loc_password_input = (By.XPATH, "//input[contains(@placeholder, 'Password')]")
    loc_tenant = (By.XPATH, "//input[contains(@placeholder, 'Select')]")
    loc_tenant_YCJ = (By.XPATH, "//ul//span[text()='YCJ']")
    loc_tenant_FA = (By.XPATH, "//ul//span[text()='FA']")
    loc_tenant_DC = (By.XPATH, "//ul//span[text()='DC']")
    loc_tenant_RA = (By.XPATH, "//ul//span[text()='RA']")
    loc_tenant_TAX = (By.XPATH, "//ul//span[text()='TAX']")
    loc_login_submit = (By.XPATH, "//div[@class='login-btn']")

    # Functions
    def input_user_name(self, name):
        self.find_element(*self.loc_name_input).send_keys(name)

    def input_password(self, password):
        self.find_element(*self.loc_password_input).send_keys(password)

    def show_tenant_list(self):
        self.find_element(*self.loc_tenant).click()
        self.wait(2)

    def choose_tenant(self, tenant_code):
        """
        passing FA, DC, RA, TAX, YCJ based environment.
        """
        if tenant_code == 'FA':
            self.find_element(*self.loc_tenant_FA).click()
        elif tenant_code == 'DC':
            self.find_element(*self.loc_tenant_DC).click()
        elif tenant_code == 'RA':
            self.find_element(*self.loc_tenant_RA).click()
        elif tenant_code == 'TAX':
            self.find_element(*self.loc_tenant_TAX).click()
        else:
            self.find_element(*self.loc_tenant_YCJ).click()

    def login(self):
        self.find_element(*self.loc_login_submit).click()
