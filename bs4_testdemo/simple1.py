#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/7 01:20'

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

if r.status_code == 200:
    soup = BeautifulSoup(r.text, "lxml")
    # soup = BeautifulSoup(r.text, "html.parser")  # 这个是python3.5自带的网页解析器,也可以用,还有其它的解析器，如：html5lib

    # print(soup)  # 格式凌乱一些
    # print(soup.prettify())   # 能按照标准的缩进格式的结构输出

    print("soup.title --> %s" % soup.title)
    print("soup.title.name --> %s" % soup.title.name)
    print("soup.title.string --> %s" % soup.title.string)
    print("soup.title.parent.name --> %s" % soup.title.parent.name)
    print("soup.p --> %s" % soup.p)
    # print(soup.p['class'])   不能用，因为上面获取的p里面无其他内容了
    print("-----Get div tree-----")
    print("soup.div --> %s" % soup.div)
    print("-----Get div class tree-----")
    print("soup.div['class']" % soup.div['class'])
    print("+++" * 30)
    print("soup.a --> %s" % soup.a)
    print("-----USE find_all()-----")
    print("soup.find_all('a') --> %s" % soup.find_all('a'))
    print("-----USE find()-----")
    print("soup.find(class_='eventList') --> %s" % soup.find(class_='eventList'))

    print("")
    print("+++" * 30)
    print("从文档中找到所有<a>标签的链接:")

    for link in soup.find_all('a'):
        print(link.get('href'))

    print("+++" * 30)
    # print("从文档中获取所有文字内容:")
    # print(soup.get_text())
    print("+++++ Test ++++++")
    print(soup.find(text="下一页"))
    print(soup.find(text="上一页"))
    print(soup.find(text="首页"))

    print("+++" * 30)
    # print(soup.find_all(class_='eventList'))
    i = 0
    for _each in soup.find_all(class_='eventList'):
        i += 1
        print("第{}个class=eventList>>>>>>>>>>".format(i))
        print(_each)

    print("+++" * 30)
    # 'data-href'

else:
    print("Response status code error! Please check it!")
