#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-13 17:46'

"""
https://docs.python.org/3/library/typing.html
"""



def greeting(name: str) -> str:
    return "Hello " + name


# 入参和返回值都加上function annotation和 import typing之后，结合PyCharm， 几乎避免所有的编译错误和入参类型不匹配。
from typing import List, Dict
def func() -> List[Dict[str, int]]:
    return [{"test": 99}]

if __name__ == '__main__':
    print(greeting("devops"))
