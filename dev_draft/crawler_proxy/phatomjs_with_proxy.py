#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/8 20:35'

from fake_useragent import UserAgent

from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import random

ua = UserAgent()

# 要是高匿代理才可以 http://www.xicidaili.com/nn/

PROXY_POOL_HTTP = ["58.53.128.83:3128", "61.135.217.7:80"]
PROXY_POOL_HTTPS = ["124.226.192.215:41193", "223.240.218.29:8118", "117.88.217.18:8118", "115.225.58.242:8118"]
PROXY_POOL = ["58.53.128.83:3128", "61.135.217.7:80"]


def get_proxy_ip_port():

    return random.sample(PROXY_POOL, 1)[0]

# service_args = [
#     '--proxy=%s' % get_proxy_ip_port(),    # 代理 IP：prot    （eg：192.168.0.28:808）
#     '--proxy-type=http',            # 代理类型：http/https
#     '--load-images=no',           # 关闭图片加载（可选）
#     '--disk-cache=yes',            # 开启缓存（可选）
#     '--ignore-ssl-errors=true'    # 忽略https错误（可选）
# ]
# # no function

dcap = dict(DesiredCapabilities.PHANTOMJS)

# 从FakeUA列表中随机选一个浏览器头，伪装浏览器
dcap["phantomjs.page.settings.userAgent"] = ua.random

# 不载入图片，爬页面速度会快很多
dcap["phantomjs.page.settings.loadImages"] = False

# 设置代理
# service_args = ['--proxy=127.0.0.1:9999', '--proxy-type=socks5']
service_args = ['--proxy={}'.format(get_proxy_ip_port()), '--proxy-type=http']
print("server_args {}".format(service_args))
# service_args = ['--proxy=58.53.128.83:3128', '--proxy-type=http']   # success, 要用高匿代理

driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=service_args)

# driver.start_session(DesiredCapabilities.PHANTOMJS)

print(dcap)

# driver.get('http://httpbin.org/ip')
driver.get("https://httpbin.org/get?show_env=1")
# driver.get("http://2018.ip138.com/ic.asp")
driver.set_page_load_timeout(10)

print('1: ', driver.session_id)
print('2: ', driver.page_source)
print('3: ', driver.get_cookies())

driver.get_screenshot_as_file('01.png')
driver.quit()

# pip install Pillow -i https://pypi.douban.com/simple
from PIL import Image

im = Image.open('01.png')
im.show()



