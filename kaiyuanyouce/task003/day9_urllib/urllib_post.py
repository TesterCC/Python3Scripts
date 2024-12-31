#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/9 00:08'

"""
http://www.jb51.net/article/93125.htm

可以发现除了第一个参数可以传递URL之外，我们还可以传递其它的内容，比如 data （附加参数）， timeout （超时时间）等等。
data 参数是可选的，如果要添加 data ，它要是字节流编码格式的内容，即 bytes 类型，通过 bytes() 函数可以进行转化，
另外如果你传递了这个 data 参数，它的请求方式就不再是 GET 方式请求，而是 POST 。
"""

import urllib.parse
import urllib.request

print("用urlopen发送post：")
rdata = {'hello': '测试'}
print(type(rdata))
print(isinstance(rdata, dict))

data = bytes(urllib.parse.urlencode({'hello': '测试'}), encoding='utf8')

# POST data should be bytes or an iterable of bytes
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())
print(type(response.read()))

print('---' * 30)
print("重点另一种POST：")

url = "http://httpbin.org/post"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
data = bytes(urllib.parse.urlencode({'hello2': '测试2'}), encoding='utf8')

req = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(req)
print(response.status, response.reason)
the_page = response.read()  # return bytes class
print(the_page.decode("unicode_escape"))

"""
先检查text是什么类型
如果type(text) is bytes，那么text.decode('unicode_escape')
如果type(text) is str，那么text.encode('utf-8').decode('unicode_escape')
"""


