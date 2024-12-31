#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/2 13:28'

"""
19-生成器-3-强调
20-生成器-4-完成多任务
"""


def test():
    i = 0
    while i < 5:
        if i == 0:
            temp = yield i
            print(temp)
        else:
            yield i
        i += 1


if __name__ == '__main__':
    t = test()
    print(t.__next__())  # 0
    print(t.send("haha"))  # haha
    print(t.__next__())  # 1
    print(t.send("haha"))  # 2
    print(t.__next__())  # 3    # yield i -> 4
