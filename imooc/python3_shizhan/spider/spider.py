#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/7 09:23'

"""
Chapter 13 spider
panda TV data crawler

Target: https://www.panda.tv/cate/lol

Notes:
爬虫前奏:
1.明确目的
2.找到数据对应的网页
3.分析网页的结构找到数据所在的标签位置
4.模拟HTTP请求， 并向服务器发送，获取到服务器返回给发送方的信息
5.使用正则表达式提取需要的数据（如: 名字、人气, etc.）
"""

from urllib import request


class Spider:
    url = 'https://www.panda.tv/cate/lol'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()

    def go(self):
        self.__fetch_content()
