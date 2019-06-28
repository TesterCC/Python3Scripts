#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-28 16:36'

"""
P68 散列表 hash table

散列表适合于:
1.模拟映射关系；
2.防止重复;
3.缓存/记住数据，以免服务器再通过处理来生产它们
"""

# 简单的缓存业务逻辑
# cache = {}
cache = {"www.test.com":"data in cache"}


def get_data_from_server(url):
    data = "data from server"
    return data


def get_page(url):
    if cache.get(url):
        return cache[url]  # 如果url存在，返回缓存数据
    else:
        data = get_data_from_server(url)
        cache[url] = data  # 先将数据保存到缓存中
        # print(cache)
        return cache

if __name__ == '__main__':
    print(get_page("www.163.com"))
    print(get_page("www.test.com"))

