#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-11 18:00'

import os
import re


file_name = "file.txt"

# file path
# print(os.path.abspath(__file__))

# file dir
# print("The folder path %s " % os.getcwd())

# needed
file_path = os.getcwd() + "/" + file_name
# print("file_path is %s" % file_path)


with open(file_path, 'r') as f:
    # 调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
    txt_content = f.read()
    f.close()

print("*"*60)


'''
re.match与re.search的区别
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
而re.search匹配整个字符串，直到找到一个匹配。

re.findall
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。

注意： match 和 search 是匹配一次 , findall 匹配所有。

此场景应该用re.findall

'''
# python use regex
# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
# 那 ?: 的作用就是把捕获分组转变为非捕获分组。
pattern = re.compile(r"(\d{3}-|\(\d{3}\)\s)\d{3}-\d{4}")   # 注意文本汇中不要匹配首尾)
pattern2 = re.compile(r"(?:\d{3}-|\(\d{3}\)\s)\d{3}-\d{4}")   # ?: 把捕获组转变为一个非捕获组，使得这个式子可以从头到尾全部匹配

'''
若匹配成功，match()/search()返回的是Match对象，finditer()返回的也是Match对象的迭代器，
获取匹配结果需要调用Match对象的group()、groups或group(index)方法。
'''
# method 1
ret = pattern.finditer(txt_content)

ret_list = [i.group() for i in ret]
print(ret_list)

# method 2
print(pattern2.findall(txt_content))