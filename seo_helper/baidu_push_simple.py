#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-10-11 10:47'


import requests

"""
https://ziyuan.baidu.com
url push
9999/day?

simple push
"""

SITE_DOMAIN = ""
SITE_TOKEN = ""

BD_PUSH_URL = 'http://data.zz.baidu.com/urls?site={}&token={}'.format(SITE_DOMAIN,SITE_TOKEN)

headers = {
    'Content-Type': "text/plain",
    'cache-control': "no-cache"
    }

need_push_urls = ['https://xxx.com/it/', 'https://xxx.com/pe/','https://xxx.com/gift/']
data = "\n".join(need_push_urls)

response = requests.post(BD_PUSH_URL, data=data, headers=headers)

print(response.text)


