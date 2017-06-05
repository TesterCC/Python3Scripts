# coding:utf-8
# python网络数据采集
# P7
# http://pythonscraping.com/pages/page1.html


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), "html.parser")  # different from book, need add "html.parser"
print(bsObj.h1)
print(bsObj.head)


