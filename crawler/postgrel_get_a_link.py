#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-04-19 19:53'

"""
task: 

用python原生库爬取https://www.postgresql.org/上所有的a link
所有links放到一个txt文件中
"""

import urllib.request
import re

target_url = "https://www.postgresql.org"

ret = urllib.request.urlopen(target_url, timeout=15)

data = ret.read()

# print(data)  # bytes

content = data.decode('utf-8')

# print(content,type(content))

"""
正则表达式：

href+连接文字 : <a.+?href="(.+?)".*>(.+)
单独href: <a.+?href="(.+?)".*>    # correct

href多信息匹配：<a.*?href="(.+)".*?>(.*?)</a>
"""

pattern = '<a.+?href="(.+?)".*>' # python3用正则获取href

"""
用re.search可以查找到第一个

用re.findall可以查找到所有的
"""
ret = re.findall(pattern, content)

pattern_2 = '^/.*'

new = [target_url+ re.findall(pattern_2,i)[0] for i in ret if re.findall(pattern_2,i)]

new_urls = []
for i in ret:
    if re.findall(pattern_2,i):
        ret_url = target_url + re.findall(pattern_2, i)[0]
        new_urls.append(ret_url)
    else:
        new_urls.append(i)

# 斜杠开头的加域名
# print(ret)
print(new_urls)

with open("postgrel_links.txt","w+") as f:
    # for i in ret:
    for i in new_urls:
        f.write(i+"\n")