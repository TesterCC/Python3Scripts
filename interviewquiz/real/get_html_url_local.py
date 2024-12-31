#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-25 14:25'

"""
问题：使用python原生库（不能用第三方库，如request提取网页中所有连接）

正则还是有点问题，需要调整
"""

import re

def get_html_link():
    pattern = '<a.*?href="(.+)".*?>(.*?)</a>'
    with open("test.html", "r") as fp:
        for line in fp:
            ret = re.search(pattern, line)
            if ret:
                for x in ret.groups():
                    print(x)


if __name__ == '__main__':
    get_html_link()
