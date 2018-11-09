#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/8 21:26'

import random

from selenium import webdriver
from fake_useragent import UserAgent

ua = UserAgent()


# HTTPS PROXY  http://www.xicidaili.com/nn/  1109S
PROXY_POOL_HTTP = ["58.53.128.83:3128", "61.135.217.7:80"]
PROXY_POOL_HTTPS = ["124.226.192.215:41193", "223.240.218.29:8118", "117.88.217.18:8118", "115.225.58.242:8118"]
# PROXY_POOL = ["58.53.128.83:3128", "61.135.217.7:80"]
PROXY_POOL = ["123.7.61.8:53281", "117.88.217.18:8118"]


def get_proxy_ip_port():
    return random.sample(PROXY_POOL, 1)[0]


proxy_ip = get_proxy_ip_port()
print(proxy_ip)

# http://www.php.cn/python-tutorials-358842.html   # firefox method2
# https://www.cnblogs.com/lgh344902118/p/6339378.html
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
# http proxy
# profile.set_preference('network.proxy.http', proxy_ip.split(":")[0])
# profile.set_preference('network.proxy.http_port', proxy_ip.split(":")[1])
# https proxy
profile.set_preference('network.proxy.ssl', proxy_ip.split(":")[0])
profile.set_preference('network.proxy.ssl_port', int(proxy_ip.split(":")[1]))    # attention port is int
profile.set_preference("general.useragent.override", ua.random)

profile.update_preferences()

#火狐无头模式
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Firefox(firefox_profile=profile, firefox_options=options)
# driver.get('http://httpbin.org/ip')
driver.get("https://httpbin.org/get?show_env=1")

print(driver.page_source)

driver.quit()
