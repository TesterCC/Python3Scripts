# coding:utf-8

# python网络数据采集 P3
# http://pythonscraping.com/pages/page1.html
# https://docs.python.org/3/library/urllib.html

from urllib.request import urlopen

html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())