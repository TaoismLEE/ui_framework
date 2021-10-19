# -*- coding:utf-8 -*-
import unittest
from lib.common.webdriver import initialize_browser
from lib.common.project_functions import open_project, login_system

# data structure defined for below test case


class CaseClassName(unittest.TestCase):
    """
    enter some description about the test case
    """
    def setUp(self):
        self.driver = initialize_browser()

    def testCaseName(self):
        home_page = open_project(self.driver)
        login_system(home_page)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
