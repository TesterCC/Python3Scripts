#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/17 22:35'


"""
《Python+Cookbook》第三版中文v3.0.0
1.3 保留最后N个元素

问题:在迭代操作或者其他操作的时候,怎样只保留最后有限几个元素的历史记录?
"""

# 保留有限历史记录正是collections.deque大显身手的时候。

from collections import deque

# break point debug
# import pdb
# pdb.set_trace()
# python -m pdb target.py
#
# import ipdb
# ipdb.set_trace()
# or use it --->    from ipdb import set_trace; set_trace()
# python target.py

'''
解决方案：
保留有限历史记录正是 collections.deque大显身手的时候。
比如,在多行上面做简单的文本匹配,并返回匹配所在行的最后N行。
'''

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a flie
if __name__ == '__main__':
    with open(r'./1_3_somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

