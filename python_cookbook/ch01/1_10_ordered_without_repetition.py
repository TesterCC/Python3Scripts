#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/6 09:37'

"""
1.10 删除序列中相同元素并保持顺序

问题：怎样在一个序列上面保持元素顺序的同时消除重复的值。


解决方案：
Method 1: 如果序列上的值都是hashable类型，那么可以很简单的利用集合或者生成器来解决这个问题。

"""


# Method 1: 如果序列上的值都是hashable类型，那么可以很简单的利用集合或者生成器来解决这个问题。
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    result = list(dedupe(a))
    print(result)
