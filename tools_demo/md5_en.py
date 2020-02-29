#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-02-29 10:36'

# 由于MD5模块在python3中被移除,故在python3中使用hashlib模块进行md5操作

import hashlib


print("*"*10 + "method 1" + "*"*10)
# 待加密信息
str = 'this is a md5 test.'

# 创建md5对象
m = hashlib.md5()

# Tips
# 此处必须encode
# 若写法为m.update(str)  报错为： Unicode-objects must be encoded before hashing
# 因为python3里默认的str是unicode
# 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
b = str.encode(encoding='utf-8')
m.update(b)
str_md5 = m.hexdigest()

print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + str_md5)

print("*"*10 + "method 2" + "*"*10)
# 另一种写法：b‘’前缀代表的就是bytes
str_md5 = hashlib.md5(b'this is a md5 test.').hexdigest()
print('MD5加密后为 ：' + str_md5)


## test
str_md5_2 = hashlib.md5(b'your string').hexdigest()
print(str_md5_2)
