# -*- coding:utf-8 -*-
from selenium import webdriver


def browser_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def browser_firefox():
    driver = webdriver.Firefox()
    driver.maximize_window()
    return driver


def browser_edge():
    driver = webdriver.edge()
    driver.maximize_window()
    return driver


def initialize_browser():
    return browser_chrome()
