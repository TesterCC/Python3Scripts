#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/3 18:02'


import re
import requests

# CAT_URL = "https://www.huodongjia.com/it/"
CAT_URL = "https://www.huodongjia.com/medical/"


# 获取网页内容
r = requests.get(CAT_URL)
data = r.text


# 利用正则查找所有event连接
# 1.先找到 https://www.huodongjia.com/event-1322992792.html，
# 2.然后拼接成 json， https://www.huodongjia.com/event-1322992792.html?json=1
DOMAIN_URL = "https://www.huodongjia.com/"
link_list = re.findall(r"event-\d{10}.html", data)    # 匹配event-{old_event_id}

event_list = []
for event_id in link_list:
    url = DOMAIN_URL + event_id + "?json=1"
    # print(url)
    event_list.append(url)

print(event_list)
print(len(event_list))

# 分页
# https://www.huodongjia.com/medical/page-1/
# https://www.huodongjia.com/medical/page-6/


CAT_URL = "https://www.huodongjia.com/medical/page-{}".format()
# https://blog.csdn.net/u010839779/article/details/77346254
