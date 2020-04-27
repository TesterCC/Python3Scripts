#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-04-27 09:50'

"""
leetcode探索：在 FIFO 数据结构中，将首先处理添加到队列中的第一个元素。

队列是典型的 FIFO 数据结构。
插入（insert）操作也称作入队（enqueue），新元素始终被添加在队列的末尾。 
删除（delete）操作也被称为出队（dequeue)。 你只能移除第一个元素。


同栈一样，队列也可以用顺序表或者链表实现。
Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小

自己写的，和给出的例子写法不同
"""

class Queue(object):
    """
    用Python实现队列
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        """
        入队
        :param item:
        :return:
        """
        # self.items.insert(0, item)
        self.items.append(item)

    def dequeue(self):
        """
        出队
        :return:
        """
        self.items.pop(0)

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("test")

    print(q.size())
    print(q.items)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.items)
    print(q.size())
