#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/19 17:37'

"""
手撕循环双端链表
现理解  循环双端链表  的概念，再来实现
首尾循环相连
https://www.bilibili.com/video/BV1ZE411P7ov?p=7

practice：
https://leetcode.com/problems/lru-cache/description/
"""


class Node:

    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class CircualDoubleLinkedList:

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        """
        获取root节点的下一个节点
        :return:
        """
        return self.root.next

    def tailnode(self):
        """
        :return:
        """
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("full")

        node = Node(value=value)
        tailnode = self.tailnode()

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("full")

        node = Node(value=value)
        # 如果为空，则自己指向自己
        if self.root.next is self.root:
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            # 不为空，则把当前节点指向 头节点
            node.prev = self.root
            headnode = self.root.next
            node.next = headnode
            headnode.prev = node
            self.root.next = node

        self.length += 1

    def remove(self, node):  # O(1), because node isn't a value, it is a node.
        # 如果是根节点，什么都不做
        if node is self.root:
            return
        else:
            # 如果是非根节点
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root: # 如果不是tailnode
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        """
        实现反向遍历
        :return:
        """
        if self.root.prev is self.root:
            return
        curnode = self.root.prev # tailnode
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode

# 开始写最复杂的步骤，单元测试
def test_double_link_list():
    cdll = CircualDoubleLinkedList()
    assert len(cdll) == 0

    cdll.append(0)
    cdll.append(1)
    cdll.append(2)

    assert list(cdll) == [0,1,2]

    # 测试遍历
    assert [node.value for node in cdll.iter_node()] == [0,1,2]
    # 测试反向遍历
    assert [node.value for node in cdll.iter_node_reverse()] == [2,1,0]

    headnode = cdll.headnode()
    assert headnode.value == 0
    cdll.remove(headnode)  # O(1) , remove node
    assert len(cdll) == 2
    assert [node.value for node in cdll.iter_node()] == [1,2]

    cdll.appendleft(0)
    assert [node.value for node in cdll.iter_node()] == [0, 1, 2]

    # Unit tset finished