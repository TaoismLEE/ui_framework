# -*- coding:utf-8 -*-
from selenium import webdriver
from conf.global_var import PROJECT_PATH


def browser_chrome():
    driver_path = PROJECT_PATH + u'/lib/' + 'chromedriver.exe'
    driver = webdriver.Chrome(driver_path)
    driver.maximize_window()
    return driver


def browser_firefox():
    driver_path = PROJECT_PATH + u'/lib/' + 'geckodriver.exe'
    driver = webdriver.Firefox(driver_path)
    driver.maximize_window()
    return driver


def browser_edge():
    driver_path = PROJECT_PATH + u'/lib/' + 'msedgedriver.exe'
    driver = webdriver.Edge(driver_path)
    driver.maximize_window()
    return driver


def initialize_browser():
    return browser_edge()
