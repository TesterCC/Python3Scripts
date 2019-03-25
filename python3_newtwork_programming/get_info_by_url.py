#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-25 17:15'

"""
用python提取url链接中的域名与端口
"""
from urllib import parse


def get_info_by_url(url):
    protocol, rest = parse.splittype(url)
    host, path = parse.splithost(rest)
    return protocol, host, path


if __name__ == '__main__':
    url = "https://www.postgresql.org/docs/9.6/index.html"
    print(get_info_by_url(url))
