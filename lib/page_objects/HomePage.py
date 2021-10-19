# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from lib.page_objects.BasePage import BasePage
from lib.common.log import logger


class HomePage(BasePage):
    """
    home page, each page can be maintain as a class inheriting from BasePage
    Locators: maintain elements locators of current page
    Functions: maintain functions can perform on current page
    """

    # Locators
    loc_language_chinese = (By.XPATH, "//ul[@class='top_bar_common']//span[text()='中文']")
    loc_language_english = (By.XPATH, "//ul[@class='top_bar_common']//span[text()='English']")
    loc_top_bar = (By.XPATH, "//ul[@class='top_bar_common']")
    loc_nav_project_management = (By.XPATH, "//div[@class='menu-wrapper']//span[text()='Project Management']")
    loc_nav_project_documentation = (By.XPATH,
                                     "//div[@class='el-submenu__title' and ./span[text()='Project Documentation']]")
    loc_sub_nav_menu = (By.XPATH, "//ul[contains(@class, 'el-menu--inline') and .//span[text()='Project Files']]")
    loc_sub_nav_project_files = (By.XPATH, "//ul[contains(@class, 'el-menu--inline')]//span[text()='Project Files']")
    loc_sub_nav_toolkit_application = (By.XPATH,
                                       "//ul[contains(@class, 'el-menu--inline')]//span[text()='Toolkit Application']")
    loc_pm_pname_search = (By.XPATH,
                           "//div[contains(@class, 'el-col-8') and ./span[.='Project Name]]/following-sibling::div/input")
    loc_pm_pcode_search = (By.XPATH, )
    loc_pm_pstatus_search = (By.XPATH, )
    loc_pm_cname_search = (By.XPATH, )
    loc_pm_ccode_search = (By.XPATH, )
    loc_pm_tmember_search = (By.XPATH, )
    loc_pm_search_reset = (By.XPATH, "//div[@class='btn-box']/span[.='Reset']")
    loc_pm_search_button = (By.XPATH, "//div[@class='btn-box']/span[.='Search']")
    loc_pm_search_arrow = (By.XPATH, "//div[@class='btn-box']/i")

    loc_pm_create_button = (By.XPATH, "//ul[@class='button-list']//span[.='Create']")
    loc_pm_export_button = (By.XPATH, "//ul[@class='button-list']//span[.='Export']")

    # Functions
    def check_top_bar_exist(self):
        return self.find_element_which_visible(*self.loc_top_bar)

    def choose_english(self):
        element = self.find_element(*self.loc_language_english)
        if element:
            element.click()
            self.wait(1)

    def head_project_management_list_page(self):
        self.find_element(*self.loc_nav_project_management).click()

    def unwrap_project_documentation_menu(self):
        element = self.find_element(*self.loc_nav_project_documentation)
        project_documentation_attri = self.get_element_attribute_value('style', *self.loc_sub_nav_menu)
        if project_documentation_attri == "display: none;":
            element.click()
            self.wait(1)

    def click_create(self):
        self.find_element(*self.loc_pm_create_button).click()
