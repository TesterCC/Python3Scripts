#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/8 20:33'


import random
import requests

from fake_useragent import UserAgent

ua = UserAgent()

# HTTPS PROXY  http://www.xicidaili.com/nn/  1109S
PROXY_POOL_HTTP = ["58.53.128.83:3128", "118.190.95.35:9001", "124.235.135.166:80"]
PROXY_POOL_HTTPS = ["124.226.192.215:41193", "223.240.218.29:8118", "117.88.217.18:8118", "115.225.58.242:8118"]
PROXY_POOL = ["223.240.218.29:8118", "123.7.61.8:53281"]

# print(ua.random)

def get_proxy_ip_port():

    return random.sample(PROXY_POOL, 1)[0]


proxy_ip = "http://" + get_proxy_ip_port()
print(proxy_ip)

proxies = {
  "http": proxy_ip,
  "https": proxy_ip,  # user https need both
}


# 'http://httpbin.org/ip'
# 'http://2018.ip138.com/ic.asp'
resp = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=7)  # return origin

# print(resp.content)
print(resp.text)
# print(type(resp.text))







