#!/usr/bin/env python
#coding=utf-8

'''
python网络数据采集  P13
http://pythonscraping.com/pages/warandpeace.html
'''


from urllib.request import urlopen
from bs4 import  BeautifulSoup


TARGET_URL = "http://pythonscraping.com/pages/warandpeace.html"

html = urlopen(TARGET_URL)
bsObj = BeautifulSoup(html, "html.parser")
# print(bsObj)

nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text())

print("----------------------")