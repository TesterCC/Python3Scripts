import os
import re
import subprocess
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def basic_options():
    options = get_default_chrome_options()
    driver = webdriver.Chrome(options=options)

    driver.quit()


def basic_set_args():
    options = get_default_chrome_options()

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)  # mac no need use chromedriver
    driver.get('http://bing.com')

    print(driver.current_url)
    print(driver.current_window_handle)

    driver.quit()

def get_default_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    return options

if __name__ == '__main__':
    basic_set_args()