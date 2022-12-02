#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "http://10.0.0.254/login"

driver = webdriver.Firefox()

driver.get(url)

# print(driver.page_source)
el_username = driver.find_element(By.NAME, 'param[UserName]')  # Find the search box
el_username.send_keys("your_username")
el_password = driver.find_element(By.NAME, 'param[UserPswd]')  # Find the search box
el_password.send_keys("your_password")
el_login_btn = driver.find_element(By.ID, 'btn_login')
el_login_btn.click()

print(driver.window_handles)
# driver.quit()
