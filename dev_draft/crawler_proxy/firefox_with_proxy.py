#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/8 21:26'


from selenium import webdriver

import random

# HTTPS PROXY  http://www.xicidaili.com/nn/  1109S
PROXY_POOL_HTTP = ["58.53.128.83:3128", "61.135.217.7:80"]
PROXY_POOL_HTTPS = ["124.226.192.215:41193", "223.240.218.29:8118", "117.88.217.18:8118", "115.225.58.242:8118"]
PROXY_POOL = ["58.53.128.83:3128", "61.135.217.7:80"]


def get_proxy_ip_port():

    return random.sample(PROXY_POOL, 1)[0]

#火狐无头模式
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Firefox(firefox_options=options)
driver.get('http://httpbin.org/ip')
# driver.get("https://httpbin.org/get?show_env=1")

print(driver.page_source)

driver.quit()
