#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/6 09:37'

"""
1.10 删除序列中相同元素并保持顺序

问题：怎样在一个序列上面保持元素顺序的同时消除重复的值。


解决方案：
Method 1: 如果序列上的值都是hashable类型，那么可以很简单的利用集合或者生成器来解决这个问题。

Method 2: 如果你想消除元素不可哈希(比如dict类型)的序列中重复元素的，参数指定了一个函数，将序列元素转换成hashable类型。
          如果想基于单个字段、属性或者某个更大的数据结构来消除重复元素，第二种方案同样可以胜任。
"""


# Method 1: 如果序列上的值都是hashable类型，那么可以很简单的利用集合或者生成器来解决这个问题。
# Method 2: 参数指定了一个函数，将序列元素转换成hashable类型。
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    result = list(dedupe(a, key=lambda d: (d['x'], d['y'])))
    print(result)
    result = list(dedupe(a, key=lambda d: d['x']))
    print(result)
