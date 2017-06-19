#!/usr/bin/env python
# coding=utf-8

'''
精通Python网络爬虫
4-2 快速使用Urllib爬取网页
'''

import urllib.request


TARGET_URL = "https://testerhome.com/"
file = urllib.request.urlopen(TARGET_URL)
data = file.read()    # read all web page content
dataline = file.readline()    # read a line of web page content
datalines = file.readlines()

print(data)
print("------------------------------")
print(dataline)
print("------------------------------")
print(datalines)

