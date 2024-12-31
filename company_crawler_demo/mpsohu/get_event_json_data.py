#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/4 09:12'


import json
import requests

"""
ignore it, just save as draft
"""

TARGET_URL = "https://www.huodongjia.com/event-1322992792.html?json=1"
DOMAIN_URL = "https://www.huodongjia.com"

# UA = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.13 Safari/537.36"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Host': 'www.huodongjia.com'
}

req = requests.get(TARGET_URL, headers=headers, timeout=10).content
print(type(req))   # python2 str, python3 bytes

# the JSON object must be str, not 'bytes'
req = req.decode("utf-8")
print(type(req))

# 将已编码的json字符串解码为Python对象
req_dict = json.loads(req)
print("req_dict type is %s" % type(req_dict))

print("遍历主要节点：")
for i in req_dict:
    print(i)

print("---" * 30)
print("遍历event主节点下的子节点：")
for key in req_dict['event']:
    print(key)

# print("{0}->{1}->{2}".format(req_dict['event_id'], req_dict['event_name'], req_dict['id']))

print("---" * 30)
print("遍历event key value：")
for k, v in req_dict['event'].items():   # req_dict['event']  type dict
    print("{0} ---> {1}".format(k, v))
    print(type(k), type(v))


def get_event_name():
    return req_dict['event']['event_name']


def get_event_url():
    event_url = DOMAIN_URL + req_dict['event']['event_url']
    return event_url


def get_id():
    return str(req_dict['event']['id'])


def get_event_begin_time():
    return req_dict['event']['event_begin_time']


if __name__ == '__main__':
    print("＊＊＊＊" * 30)
    # print(get_event_name())
    # print(get_event_url())
    # print(get_id())
    # print(get_event_begin_time())
    # print(type(get_event_img()))

