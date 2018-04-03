#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/3 14:28'

import re
import requests

TARGET_URL = "https://www.huodongjia.com/"
# 获取网页内容
r = requests.get(TARGET_URL)
data = r.text

# 利用正则查找所有连接
link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", data)
for url in link_list:
    print(url)


