# coding=utf-8
"""
DATE:   2022/1/5
AUTHOR: TesterCC
"""

"""
Python解决unicode编码 \xe7\xbb\x87转化为中文

https://blog.csdn.net/baidu_19473529/article/details/54949453
"""

s = "\xe4\xb8\xad\xe6\xb1\xbd\xe5\x88\x9b\xe6\x99\xba\xe6\xb5\x8b\xe8\xaf\x95\xe5\x8f\xb0\xe6\x9e\xb6"

print(s.encode("raw_unicode_escape").decode())