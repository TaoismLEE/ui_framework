# -*- coding:utf-8 -*-
import unittest
from lib.common.webdriver import initialize_browser
from lib.common.project_functions import open_project, login_edms
from lib.common.parse_file import ParseCSV
from lib.common.log import logger
from lib.page_objects.HomePage import HomePage
from lib.page_objects.CreateProjectPage import CreateProjectPage

# data structure defined for below test case


class YcjCreateProject(unittest.TestCase):
    """
    enter some description about the test case
    """
    def setUp(self):
        self.driver = initialize_browser()

        # get username, password
        try:
            csv_obj = ParseCSV('edms_accounts.csv')
            accounts = csv_obj.read_csv()
            self.user_name = accounts[1][1]
            self.user_password = accounts[1][2]
        except Exception as e:
            logger.error("Failed to open data file!")
            logger.error(e)

    def testYcjCreateProject(self):
        login_page = open_project(self.driver)
        login_edms(login_page, "YCJ", self.user_name, self.user_password)
        home_page = HomePage(login_page.driver)
        home_page.choose_english()
        home_page.head_project_management_list_page()
        home_page.click_create()
        create_page = CreateProjectPage(home_page.driver)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
