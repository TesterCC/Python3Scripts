#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-25 14:25'


"""
问题：使用python原生库（不能用第三方库，如request提取网页中所有连接）

降低难度类：python3用BeautifulSoup用字典的方法抓取a标签内的数据 (草稿)

目标：https://www.postgresql.org/docs/9.6/index.html
"""

import re
from urllib import request
from bs4 import BeautifulSoup
import traceback


def get_html_link(target_url):
    domain = "https://www.postgresql.org"
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")
    opener = request.build_opener()
    opener.addheaders = [headers]
    request.install_opener(opener)

    html = request.urlopen(target_url).read()
    # html = html.decode('utf-8')

    # print(html)

    # pattern = '<a.*?href="(.+)".*?>(.*?)</a>'
    # for line in html:
    #     ret = re.search(pattern, line)
    #     if ret:
    #         for x in ret.groups():
    #             print(x)

    soup = BeautifulSoup(html, 'html.parser')
    for k in soup.find_all('a'):
        # print(k)
        # print(k['class'])  # 查a标签的class属性
        # print(k['id'])  # 查a标签的id值
        try:
            # print(k['href'])  # 查a标签的href值
            print(k['href'])  # 查a标签的href值
        except Exception as err:
            traceback.print_exc()

        # print(k.string)  # 查a标签的string

if __name__ == '__main__':
    url = "https://www.postgresql.org/docs/9.6/index.html"
    get_html_link(url)

