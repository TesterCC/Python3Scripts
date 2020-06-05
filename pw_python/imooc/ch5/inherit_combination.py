#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/4 17:15'

'''
用组合实现stack/queue
'''

from collections import deque

class Stack:   # 使用组合的例子
    def __init__(self):
        self._deque = deque()   # has a deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def empty(self):
        return len(self._deque) == 0


