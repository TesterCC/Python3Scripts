#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/8 22:50'

import random
from urllib import request

PROXY_POOL = ["223.240.218.29:8118", "123.7.61.8:53281"]


def get_proxy_ip_port():
    return random.sample(PROXY_POOL, 1)[0]


if __name__ == "__main__":
    # 访问网址
    url = 'http://httpbin.org/ip'
    # 这是代理IP
    # proxy = {'https': '123.7.61.8:53281'}   # can use
    proxy = {'https': '175.148.72.86:1133'}   # for test
    # 创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    # 创建Opener
    opener = request.build_opener(proxy_support)
    # 添加User Angent
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    # 安装OPener
    request.install_opener(opener)
    # 使用自己安装好的Opener
    response = request.urlopen(url)
    # 读取相应信息并解码
    html = response.read().decode("utf-8")
    # 打印信息
    print(html)
