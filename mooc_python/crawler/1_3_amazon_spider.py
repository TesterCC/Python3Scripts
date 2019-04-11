#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-11 16:27'

import requests

"""
爬亚马逊单页面(现在没有拦截)

注意：
print(req.encoding)结果显示ISO-8859-1
之所以会有ISO-8859-1这种编码是因为：
requests会从服务器返回的响应头的 Content-Type 去获取字符集编码，如果content-type有charset字段那么requests才能正确识别编码，
否则就使用默认的 ISO-8859-1. 一般那些不规范的页面往往有这样的问题. 

解决办法：
requests的返回结果对象里有个apparent_encoding函数, apparent_encoding通过调用chardet.detect()来识别文本编码


关于requests后面跟的text() 与content() 的区别：

r.text返回的是处理过的Unicode型的数据，而使用r.content返回的是bytes型的原始数据。
也就是说，r.content相对于r.text来说节省了计算资源，r.content是把内容bytes返回. 
而r.text是decode成Unicode. 如果headers没有charset字符集的化,text()会调用chardet来计算字符集。


"""

url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"


try:
    kv = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.status_code)
    print(r.text[:1000])
except:
    print("Crawl info failed.")