#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/7 02:59'


"""
https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
BeautifulSoup官方文档演示demo
target: https://www.huodongjia.com/it/
"""

import requests
from bs4 import BeautifulSoup


TARGET_URL = "https://www.huodongjia.com/it/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Host': 'www.huodongjia.com'
}


r = requests.get(TARGET_URL, headers=headers, timeout=10)

soup = BeautifulSoup(r.text, "lxml")

print("+++" * 30)
i = 0
for _each in soup.find_all(class_='eventList'):
    i += 1
    print(">>>>>>>>>>第{}个class=eventList>>>>>>>>>>".format(i))
    print(_each)

print("+++" * 30)

print("获取所有a下面的href：")
a_list = soup.find_all('a')
for item in a_list:
    print(item.get("href"))
print("+++" * 30)

print("---过滤所有event link---")
print("Method1:")
print("获取所有div下面的data-href,没有data-href的不打印：")
div_list = soup.find_all('div')
for item in div_list:
    if item.get("data-href"):    # get div下面的data-href
        print(item.get("data-href"))
print("---" * 30)

print("Method2-recommend:")
print("获取所有div下面的data-href,没有data-href的不打印：")
event_list = soup.find_all('div', class_="eventList")
for event_item in event_list:
    event_url = event_item.get("data-href")
    print(event_url)




