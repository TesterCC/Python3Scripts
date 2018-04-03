#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/3 18:02'


import re
import requests

CAT_URL = "https://www.huodongjia.com/it/"

# 获取网页内容
r = requests.get(CAT_URL)
data = r.text

# 利用正则查找所有event连接
# 1.先找到 https://www.huodongjia.com/event-1322992792.html，
# 2.然后拼接成 json， https://www.huodongjia.com/event-1322992792.html?json=1  PS:好好看下正则表达式，不然就只能上BS了
link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", data)
link_list = re.findall(r"^(/event-(d{10}).html)", data)
for url in link_list:
    print(url)

