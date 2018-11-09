#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/9 10:20'


"""
selenium设置chrome–cookie
REF:
https://blog.csdn.net/xc_zhou/article/details/80823855  (recommend)
"""


import random
from fake_useragent import UserAgent
from selenium import webdriver

ua = UserAgent()

# http://www.xicidaili.com/nn/
# PROXY_POOL = ["123.7.61.8:53281", "117.88.217.18:8118"]
#
# def get_proxy_ip_port():
#     return random.sample(PROXY_POOL, 1)[0]
#
# proxy_ip = get_proxy_ip_port()
# # proxy_ip = "123.7.61.8:53281"   ＃ for debug
#
# print(proxy_ip)


options = webdriver.ChromeOptions()
# options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
# options.add_argument('window-size=800x600')
# 设置伪装UA
options.add_argument('user-agent="{}"'.format(ua.random))

driver = webdriver.Chrome(chrome_options=options)
driver.get('http://httpbin.org/ip')
# driver.get("https://httpbin.org/get?show_env=1")
# driver.get("http://2018.ip138.com/ic.asp")

# 删除原来的cookie
driver.delete_all_cookies()
# set-cookies
driver.add_cookie({'name': 'ABC00','value': 'DEF01'})

print('1: ', driver.session_id)
print('2: ', driver.page_source)
print('3: ', driver.get_cookies())

# driver.get_screenshot_as_file('03.png')
driver.quit()


# pip install Pillow -i https://pypi.douban.com/simple
# from PIL import Image
#
# im = Image.open('03.png')
# im.show()