#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/20 22:29'

"""
用数据array实现队列queue

队列是先进先出结构(FIFO, first in first out)， 
栈是后进先出结构(LIFO, last in first out)。

https://www.bilibili.com/video/BV1ZE411P7ov?p=10

when-changed -r -v -1 -s ./ 'pytest -s array_queue.py'
"""

class FullError(Exception):
    pass

class Array(object):

    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


# 用数据array实现队列queue
class ArrayQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0

    def push(self,value):
        if len(self) >= self.maxsize:
            raise FullError('queue full')

        # 把value追加到array相应位置
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value

    def __len__(self):
        return self.head - self.tail


# pytest unit test
def test_array_queue():
    import pytest
    size = 5
    q = ArrayQueue(size)
    for i in range(size):
        q.push(i)

    with pytest.raises(FullError) as excinfo:
        q.push(size)
    assert "full" in str(excinfo)
    assert 'queue full' == str(excinfo.value)

    assert len(q) == size  # 5
    assert q.pop() == 0
    assert q.pop() == 1

    q.push(5)
    assert len(q) == 4

    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.pop() == 5

    assert len(q) == 0