# -*- coding:utf-8 -*-
"""
This module contains the basic but common manipulations that all pages may perform.
Eg. move forward, move back, find element, click element, etc.
"""

import os
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from lib.common.log import logger


class BasePage(object):
    """
    Base page class, all other page class inherits from this class.
    Mainly maintain basic and shared functions each page may perform.
    """

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def wait(wait_time):
        """ sleep or wait a while by force
        :wait_time: a period in second
        """
        sleep(wait_time)

    def on_page(self, url):
        """ page check by url comparing
        :url: passing the target url which to compare with current browser tab url
        :return: True or False
        """
        return self.driver.current_url == url

    def move_back(self):
        """ move back to last url in current tab"""
        self.driver.back()
        self.wait(3)

    def move_forward(self):
        """ move forward to next url in current tab"""
        self.driver.forward()
        self.wait(3)

    def open(self, url):
        """ open new page according to passed param url
        :url: target url needed to open
        """
        self.driver.get(url)

    def set_window_size(self, width, height):
        """ customize the window size to particular width and height
        :width: target browser width
        :height: target browser height
        """
        self.driver.set_window_size(width, height)

    def find_element(self, *loc):
        """ rewrite the finding element function, if the element located within 10 seconds,
        then return the element or return False
        :*loc: the locator of element
        :return: element or False if not found
        :retype: obj
        """
        try:
            return WebDriverWait(self.driver, 30, 1).until(ec.presence_of_element_located(loc))
        except TimeoutException or NoSuchElementException:
            logger.error("The element:{} has not been shown in current page!".format(str(loc)))
            return False

    def find_elements(self, *loc):
        """ rewrite the finding elements function, if the elements located within 10 seconds,
        then return the elements or return False
        :*loc: the locator of elements
        :return: lists of elements
        :retype: list
        """
        try:
            return WebDriverWait(self.driver, 30, 1).until(ec.presence_of_all_elements_located(loc))
        except TimeoutException or NoSuchElementException:
            logger.error("The elements:{} have not been shown in current page!".format(str(loc)))
            return False

    def find_element_which_visible(self, *loc):
        """ check whether the element is displayed
        :*loc: locator of element
        :return: element or False
        retype: obj
        """
        try:
            return WebDriverWait(self.driver, 30, 1).until(ec.visibility_of_element_located(loc))
        except TimeoutException or NoSuchElementException:
            logger.error("The element: {} has not shown in current page!".format(str(loc)))
            return False

    def find_element_which_clickable(self, *loc):
        """ check whether the element is clickable
        :*loc: locator of element
        :return: element
        retype: obj
        """
        try:
            return WebDriverWait(self.driver, 30, 1).until(ec.element_to_be_clickable(loc))
        except TimeoutException or NoSuchElementException:
            logger.error("The element: {} has not shown in current page or clickable!".format(str(loc)))
            return False

    def affirm_element_disappear(self, *loc):
        """ make sure the element is NOT displayed, not in the DOM
        :*loc: the locator of element
        :return: True if element disappears from DOM, else False
        :retype: boolean
        """
        try:
            return WebDriverWait(self.driver, 30, 1).until_not(ec.presence_of_element_located(loc))
        except TimeoutException:
            logger.error("The element:{} still shows in current page!".format(str(loc)))
            return False

    def get_current_window_handle(self):
        """ get the current active window tab handler: can think of it as the unique label of window tab
        :return: current active window ID
        :retype: string
        """
        return self.driver.current_window_handle

    def get_window_handles(self):
        """ get handlers of all opened windows: can think of it as the unique label of each window tab
        :return: all opened window IDs
        :retype: list of strings
        """
        return self.driver.window_handles

    def close_current_window(self):
        """ close current active window tab"""
        self.driver.close()
        self.wait(1)

    def switch_to_window(self, new_handler):
        """ swith to the specific window tab which is given with parameter
        :new_handler: the target window tab to switch
        """
        self.driver.switch_to_window(new_handler)
        self.wait(1)

    def send_keys(self, value, clear_first=True, click_first=True, *loc):
        """ simulating keyboard input to input the given value
        :clear_first: by default, clear the input box before input the value
        :click_first: by default, click the input box to active it
        :value: the text string to input
        :*loc: element locator
        """
        try:
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except Exception as e:
            logger.error("Element with locator: %s has not been found!" % str(loc))
            logger.error(e)

    def capture_page_snapshot(self, file_name):
        """ capture the screenshot to save to ./report folder with specific file_name
        :file_name: name the picture, eg. script_name.png
        """
        try:
            base_dir = os.getcwd()
            file_path = base_dir + "/report/" + file_name
            file_path = os.path.abspath(file_path)
            self.driver.get_screenshot_as_file(file_path)
        except Exception as err:
            logger.error(err)
            logger.error("Failed to save snapshot: %s" % file_name)

    def get_element_size(self, *loc):
        """ return the size of element
        :*loc: the locator of element
        :return: {'height': number, 'width': number}
        :retype: dict
        """
        return self.find_element(*loc).size

    def get_element_text(self, *loc):
        """ return the content of element
        :*loc: the locator of element
        :return: element content
        :retype: string
        """
        return self.find_element(*loc).text

    def get_url(self):
        """ return the URL of current active page
        :return: url
        :retype: string
        """
        return self.driver.current_url

    def get_title(self):
        """ return the web page title
        :return: name of active web page title
        :retype: string
        """
        return self.driver.title

    def get_element_attribute_value(self, attribute_name, *loc):
        """ return the specific value of element attribute
        :*loc: the locator of element
        :return: attribute value
        :retype: string
        """
        return self.find_element(*loc).get_attribute(attribute_name).strip()

    def right_click(self, *loc):
        """ simulating right-click on element
        :*loc: locator of target element
        """
        element = self.find_element(*loc)
        ActionChains(self.driver).context_click(element).perform()
        self.wait(1)

    def double_click(self, *loc):
        """ simulating double-click on element
        :*loc: locator of target element
        """
        element = self.find_element(*loc)
        ActionChains(self.driver).double_click(element).perform()
        self.wait(3)

    def move_to_element(self, *loc):
        """ simulating move the mouse right above the element
        :*loc: the locator of element
        """
        element = self.find_element(*loc)
        ActionChains(self.driver).move_to_element(element).perform()
        self.wait(3)

    def click_and_hold(self, *loc):
        """ simulating keep pressing an element
        :*loc: the locator of element
        """
        element = self.find_element(*loc)
        ActionChains(self.driver).click_and_hold(element).perform()

    def input_one_space(self, *loc):
        """ simulate input a space
        :*loc: the locator of element
        """
        self.find_element(*loc).send_keys(Keys.SPACE)

    def copy_all_content(self, *loc):
        """ simulate Ctrl + a
        :*loc: the locator of element
        """
        self.find_element(*loc).send_keys(Keys.CONTROL, 'a')

    def cut_all_content(self, *loc):
        """ simulate Ctrl + x
        :*loc: the locator of element
        """
        self.find_element(*loc).send_keys(Keys.CONTROL, 'x')

    def paste_all_content(self, *loc):
        """ simulate Ctrl + x
        :*loc: the locator of element
        """
        self.find_element(*loc).send_keys(Keys.CONTROL, 'v')

    def switch_to_frame(self, frame_id_value):
        """ switch to specific iframe
        :frame_id: the ID's value of iframe
        """
        self.driver.switch_to_frame(frame_id_value)
        self.wait(1)

    def accept_alert(self):
        """ accept alert, confirm or prompt generated by JavaScript
        """
        element = self.driver.switch_to_alert()
        element.accept()
        self.wait(3)

    def dismiss_alert(self):
        """ dismiss alert, confirm or prompt generated by JavaScript
        """
        element = self.driver.switch_to_alert()
        element.dismiss()
        self.wait(3)

    def get_alert_text(self):
        """ get the value of alert, confirm or prompt generated by JavaScript
        :return: alert/confirm/prompt value
        :retype: string
        """
        element = self.driver.switch_to_alert()
        element.text()

    def send_keys_to_confirm(self, value):
        """ send inputs to confirm or prompt generated by JavaScript if allowed
        :value: the value to input
        """
        element = self.driver.switch_to_alert()
        element.send_keys(value)

    def execute_js(self, js):
        """ execute js script
        :js: string of js code
        """
        self.driver.execute_script(js)

    def scroll_to_top(self):
        """ scroll to top of window"""
        js = "var q=document.documentElement.scrollTop=0"
        self.execute_js(js)

    def scroll_to_bottom(self):
        """ scroll to top of window"""
        js = "var q=document.documentElement.scrollTop=10000"
        self.execute_js(js)

    def get_cookies(self):
        """ get all cookies
        :return: all cookies as a dict list
        :retype: list
        """
        return self.driver.get_cookies()

    def get_cookie(self, cookie_name):
        """ get the specific cookie value
        :return: cookie with specific name
        :retype: dict
        """
        return self.driver.get_cookie(cookie_name)

    def add_cookie(self, cookie_dict):
        """ add cookie
        :cookie_dict: cookie at least with name:value and value:value,
        eg.{'name':'key-aaaaaaa', 'value':'value-bbbb'}
        """
        self.driver.add_cookie(cookie_dict)

    def delete_cookie(self, cookie_name):
        """ delete the specific cookie"""
        self.driver.delete_cookie(cookie_name)

    def delete_all_cookies(self):
        """ delete all cookies"""
        self.driver.delete_all_cookies()
