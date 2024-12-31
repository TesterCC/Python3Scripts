#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/10/31 15:10'


"""
Python网络爬虫--从入门到实践   P22-25 2.3 编写一个简单的爬虫
Crawler Target: www.santostang.com
"""

import requests
from bs4 import BeautifulSoup    # 从bs4这个库中导入BeautifulSoup


# Step 1 -- Get html
link = "http://www.santostang.com"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

r = requests.get(link, headers=headers)
# print(r.text)    # for Debug

# Step 2 -- Extract needed data
# soup = BeautifulSoup(r.text, "lxml")   # 使用BeautifulSoup解析这段代码   # 用lxml可能会报错，可以用python3.5自带的网页解析器
soup = BeautifulSoup(r.text, "html.parser")  # 这个是python3.5自带的网页解析器
title = soup.find("h1", class_="post-title").a.text.strip()
print(title)

# Step 3 -- Store data
with open('title.txt', "a+") as f:
    f.write(title)
    f.close()