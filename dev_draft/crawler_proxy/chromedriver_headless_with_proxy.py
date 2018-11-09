#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/8 21:04'

import random
from fake_useragent import UserAgent
from selenium import webdriver

ua = UserAgent()

# http://www.xicidaili.com/nn/
PROXY_POOL_HTTP = ["58.53.128.83:3128", "61.135.217.7:80"]
PROXY_POOL_HTTPS = ["124.226.192.215:41193", "223.240.218.29:8118", "117.88.217.18:8118", "115.225.58.242:8118"]
PROXY_POOL = ["123.7.61.8:53281", "117.88.217.18:8118"]


def get_proxy_ip_port():
    return random.sample(PROXY_POOL, 1)[0]

proxy_ip = get_proxy_ip_port()
# proxy_ip = "123.7.61.8:53281"   ＃ for debug

print(proxy_ip)
# print(random.sample(PROXY_POOL, 1))   # list
# print(random.sample(PROXY_POOL, 1))
# print(random.sample(PROXY_POOL, 1)[0])   # str


options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
# options.add_argument('window-size=1200x600')
# 设置伪装UA
options.add_argument('user-agent="{}"'.format(ua.random))
# options.add_argument('--proxy-server=http://ip:port')
options.add_argument('--proxy-server=http://{}'.format(proxy_ip))
# print('user-agent="{}"'.format(ua.random))
print('--proxy-server=http://{}'.format(proxy_ip))

print("*"*50)
print(options)

driver = webdriver.Chrome(chrome_options=options)

# driver.get('http://httpbin.org/ip')
driver.get("https://httpbin.org/get?show_env=1")
# driver.get("http://2018.ip138.com/ic.asp")
driver.set_page_load_timeout(10)

print('1: ', driver.session_id)
print('2: ', driver.page_source)
print('3: ', driver.get_cookies())

driver.get_screenshot_as_file('02.png')
driver.quit()

# pip install Pillow -i https://pypi.douban.com/simple
from PIL import Image

im = Image.open('02.png')
im.show()
