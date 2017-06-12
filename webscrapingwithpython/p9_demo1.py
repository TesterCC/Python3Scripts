#!/usr/bin/env python
#coding=utf-8

'''
python网络数据采集   P9
http://pythonscraping.com/pages/page1.html
'''


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


TARGET_URL = "http://pythonscraping.com/pages/page1.html"
# TARGET_URL = "http://asfasdfassd.com"


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle(TARGET_URL)

if title == None:
    print("Title could not be found.")
else:
    print(title)