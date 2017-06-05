# coding:utf-8
# !/usr/bin/env python

# python3
# http://www.imooc.com/video/12624

from urllib import request

resp = request.urlopen("http://www.baidu.com")

# print(resp.read())
# print(resp.read().decode("utf-8"))  -- cannot


# right way in Mac OSX
# http://blog.sina.com.cn/s/blog_eb82ea590102w2xc.html
html = str(resp.read(), 'utf-8')
print(html)