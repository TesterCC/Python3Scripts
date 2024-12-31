#!/usr/bin/env python
# coding=utf-8

'''
python网络数据采集   P18
http://pythonscraping.com/pages/page3.html
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup


# 仅仅找子标签
html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)

print(">>>----------------------------------------------<<<")


# 处理兄弟标签
html2 = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj2 = BeautifulSoup(html2, "html.parser")

for sibling in bsObj2.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

