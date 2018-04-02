#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/2 21:48'

"""
每个账号每天发5篇，无需换IP发布，但需清除cookie，发布间隔3分钟。
发布方式
http://mp.sohu.com/v2/main/news/add.action
"""

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# driver = webdriver.PhantomJS()
driver = webdriver.Chrome()

driver.get("https://mp.sohu.com/mpfe/v3/login")

login_nav = driver.find_element_by_xpath('//*[@id="mpfe"]/div[3]/div/article/div[1]/div[2]/div/div[1]/span[1]')

login_nav.click()

input_username = driver.find_element_by_xpath("//*[@id='mpfe']/div[3]/div/article/div[1]/div[2]/div/div[3]/div[1]/input")

input_username.click()

input_username.send_keys("18782291154")

input_password = driver.find_element_by_xpath("//*[@id='mpfe']/div[3]/div/article/div[1]/div[2]/div/div[3]/div[2]/input")

input_password.click()

input_password.send_keys("huodongjia123456")

submit = driver.find_element_by_xpath('//*[@id="mpfe"]/div[3]/div/article/div[1]/div[2]/div/button')

submit.click()

sleep(5)

print(driver.current_url)

after_login_page_url = "https://mp.sohu.com/mpfe/v3/main/first/page"
if driver.current_url == after_login_page_url:
    print("Login Success!")
    driver.quit()
else:
    print("Current url is incorrect!")


# try:
#     element = WebDriverWait(driver, 10).until(
#         # http://selenium-python.readthedocs.io/waits.html?highlight=Text_to_be_present_in_element
#         EC.text_to_be_present_in_element((By.XPATH, '//*[@id="mpfe"]/div[3]/div[2]/div/div[1]/ul/li[2]/a/span'), "写文章")
#     )
# finally:
#     print("Cannot find expected text in element")
#     driver.quit()











