# coding=utf-8
"""
DATE:   2021/12/21
AUTHOR: TesterCC
"""

import bson

# int转int64 NumberLong

a = bson.int64.Int64(int(1111))
print(a)
print(type(a))
