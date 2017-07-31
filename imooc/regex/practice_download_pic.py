#!/usr/bin/env python
# coding=utf-8

# http://www.imooc.com/video/10512
# python正则表达式练习

'''
抓取网页中的图片到本地：
1.抓取网页
2.获取图片地址
3.抓取图片内容并保存到本地
'''


import urllib.request   # python3 need "import urllib.request"
import re

target_url = "http://www.imooc.com/course/list"
req = urllib.request.urlopen(target_url)
buf = str(req.read())    # convert to str class, not recommand, download pic can not display

# req.read()获取的是bytes,而req.findall()是查找string里的,可以用req.read().decode("utf-8")
print(buf)


# picture url -- http://img.mukewang.com/549bda090001c53e06000338-240-135.jpg

# list_url = re.findall(r'src=.+\.jpg', buf)
list_url = re.findall(r'http://img.+?\.jpg|http://szimg.+?\.jpg', buf)   # hard code, can success, but not practical, change to start with http:

# 然而目前还不能直接一个表达式匹配出来
# list_url = re.findall(r'http:.+?\.jpg', buf)    original

# print(list_url)


# downlaod pics and save in local host
i = 0
for url in set(list_url):

    try:
        # with open("./"+str(i)+'.jpg', 'w', encoding='utf-8') as f:
        f = open("./"+str(i)+'.jpg', 'wb')    # 指定目录
        req = urllib.request.urlopen(url)
        buf = req.read()
        f.write(buf)     # buf need str classs
        print("Finish download picture: %d" % (i+1))    # for debug, can comment
        i += 1
    except Exception as e:
        print(e)



# debug code -- need delete repetition
# i = 0
# # print(set(list_url))
# for url in set(list_url):
#     print(str(i)+"--"+url)
#     i += 1




