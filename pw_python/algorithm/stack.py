#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/21 21:32'

"""
12 栈 stack
ref:
https://www.bilibili.com/video/BV1ZE411P7ov?p=12

利用循环双端队列实现Deque，
在利用Deque实现Stack

单元测试：
./pytest.sh stack.py

when-changed -r -v -1 -s ./ "pytest -s stack.py"

pytest -s stack.py
"""

from .double_link_list import CircualDoubleLinkedList

class Deque(CircualDoubleLinkedList):

    def pop(self):
        # 从右边删除一个结点
        if len(self) == 0:
            raise Exception("empty")
        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)
        return value

    def popleft(self):
        # 从左边删除一个结点
        if len(self) == 0:
            raise Exception("empty")
        headnode = self.headnode()
        value = headnode.value
        self.remove(headnode)
        return value

class Stack:
    def __init__(self):
        self.deque = Deque()     # 用Python自带的 collections.deque 实现更方便

    def push(self,value):
        return self.deque.append(value)

    def pop(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)

    def is_empty(self):
        return len(self) == 0

def test_stack():
    s = Stack()
    for i in range(3):
        s.push(i)

    assert len(s) == 3

    # stack, LIFO后进先出
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0
    assert s.is_empty()

    import pytest
    # 测试异常
    with pytest.raises(Exception) as excinfo:
        s.pop()
    assert "empty" in str(excinfo.value)

