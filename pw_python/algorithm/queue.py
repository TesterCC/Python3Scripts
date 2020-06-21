#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/19 22:55'

"""
9.队列
https://www.bilibili.com/video/BV1ZE411P7ov?p=9

FIFO  先进先出

利用之前写的单链表来实现

用工具实现变更后自动执行单元测试
when-changed -r -v -1 -s ./ 'pytest -s queue.py'
"""
from .linked_list import LinkedList  # 利用之前写的linked_list


# 用Linked List实现Queue （用链表实现队列）

class FullError(Exception):
    pass


class EmptyError(Exception):
    pass


class Queue:
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_linked_list = LinkedList()

    def __len__(self):
        return len(self._item_linked_list)

    def push(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise FullError('queue full')
        return self._item_linked_list.append(value)

    def pop(self):
        if len(self) <= 0:
            raise EmptyError('queue empty')
        return self._item_linked_list.popleft()


# 编写测试代码
def test_queue():
    q = Queue()
    q.push(0)
    q.push(1)
    q.push(2)

    assert len(q) == 3
    assert q.pop() == 0
    assert q.pop() == 1
    assert q.pop() == 2
    assert len(q) == 0

    import pytest
    with pytest.raises(EmptyError) as excinfo:
        q.pop()   # raise EmptyError
    assert 'queue empty' == str(excinfo.value)
    assert 'empty' in str(excinfo.value)

