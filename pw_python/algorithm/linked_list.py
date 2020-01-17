#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-15 13:18'

"""
5、6.单链表

特点：不连续、无法通过下标直接访问、追加元素方便(append)

时间复杂度：
https://pegasuswang.github.io/python_data_structures_and_algorithms/03_%E9%93%BE%E8%A1%A8/linked_list/
链表操作	                             平均时间复杂度
linked_list.append(value)	         O(1)
linked_list.appendleft(value)	     O(1)
linked_list.find(value)	             O(n)
linked_list.remove(value)	         O(n)

7、8.循环双端链表

"""


class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        """方便打出来调试，复杂的代码可能需要断点调试"""
        return '<Node: value: {}, next={}>'.format(self.value, self.next)

    __repr__ = __str__  # 调用p与调用print p的效果是一样的, 即调用实例变量时也会调用__str__, 不需要可以注释


class LinkedList(object):
    """ 单链表/链接表 ADT
    [root] -> [node0] -> [node1] -> [node2]
    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()  # 默认 root 节点指向 None
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):  # O(1)
        # 首先判断当前长度是否超过当前最大值  # 右、后端 tailnode
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('LinkedList is Full')

        node = Node(value)  # 通过value值构造新节点，插到最后一个节点后面
        tailnode = self.tailnode
        if tailnode is None:  # 说明只有一个root节点，还没有 append 过，length = 0， 追加到 root 后
            # 只需要把root的next节点指向当前节点
            self.root.next = node
        else:  # 否则追加到最后一个节点的后边，并更新最后一个节点是 新append 的节点
            tailnode.next = node  # 插到最后一个节点后面

        self.tailnode = node  # 更新tailnode
        self.length += 1

    def appendleft(self, value):  # O(1)
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')

        node = Node(value)  # 构造新节点
        if self.tailnode is None:  # 如果原链表为空，插入第一个元素需要设置 tailnode
            self.tailnode = node

        # 如果原链表不为空，插入到root节点的后面，链表的左、前端 headnode
        headnode = self.root.next
        self.root.next = node  # 将当前的self.root.next指向当前节点
        node.next = headnode  # 将当前节点的next节点指向原来的headnode
        self.length += 1

    def iter_node(self, ):
        """实现遍历操作, 从首节点遍历到尾节点
           遍历 从 head 节点到 tail 节点
        """
        # 第一个节点是根节点的下一个节点
        curnode = self.root.next

        while curnode is not self.tailnode:  # 从第一个节点开始遍历， 如果当前节点不是尾节点
            yield curnode
            # 然后将当前节点更新到下一个节点
            curnode = curnode.next

        if curnode is not None:  # 如果当前节点不为None
            yield curnode

    def __iter__(self):
        """实现遍历操作"""
        for node in self.iter_node():
            yield node.value

    def remove(self, value):  # O(n)
        """查找并删除某节点，时间复杂度O(n)
           让 要删除的节点的前一个节点的next节点 指向 要删除的节点的next节点
        删除包含值的一个节点，将其前一个节点的 next 指向被查询节点的下一个节点即可
        """
        prevnode = self.root

        for curnode in self.iter_node():
            if curnode.value == value:  # 查到到了要删除的值
                prevnode.next = curnode.next  # 把 前节点的next节点 指向 当前节点的next节点
                if curnode is self.tailnode:  # NOTE: 注意更新tailnode
                    if prevnode is self.root:
                        self.tailnode = None
                    else:
                        self.tailnode = prevnode
                del curnode  # 把当前节点删除
                self.length -= 1  # 当前长度减1
                return 1  # 表明删除成功
            else:  # NOTE: 更新prevnode
                prevnode = curnode  # 将已经检查过的当前节点指向前节点
        return -1  # 表明删除失效

    def find(self, value):  # O(n)
        """查找一个节点，返回序号，从 0 开始"""
        index = 0
        # 查找操作, O(n),需要遍历
        for node in self.iter_node():  # 已定义 __iter__，故这里可用 for 遍历它
            if node.value == value:
                return index  # 如果查找到值，就返回index
            index += 1  # 如果没有查找到值，index就递增继续循环查找
        return -1  # 如果没有查找到就返回-1做标识

    def popleft(self):  # O(1)，
        """
        删除第一个链表节点，删除头节点
        """
        if self.root.next is None:
            raise Exception('pop from empty LinkedList')

        headnode = self.root.next
        self.root.next = headnode.next  # 把root节点的下一个节点指向头节点的下一个节点
        self.length -= 1
        value = headnode.value  # 一般删除操作都会返回一个删除的value值

        if self.tailnode is headnode:  # 增加单节点删除 tailnode 处理
            self.tailnode = None

        del headnode  # 删除头节点
        return value

    def clear(self):
        # 用于清除链表
        for node in self.iter_node():
            del node
        self.root.next = None  # 将根节点下的下一个节点置为None值
        self.length = 0  # 链表长度置为0
        self.tailnode = None  # 将尾节点置为None值

    def reverse(self):
        """反转链表"""

        curnode = self.root.next  # 链表的头节点
        self.tailnode = curnode  # 记得更新 tailnode，多了这个属性处理起来经常忘记。将链表的头节点指想链表尾节点
        prevnode = None

        # 这段仔细理解一下
        while curnode:
            nextnode = curnode.next
            curnode.next = prevnode

            if nextnode is None:
                self.root.next = curnode

            prevnode = curnode
            curnode = nextnode


# Unittest
def test_linked_list():
    """
    cd ~/pw_python/algorithm
    pytest -s linked_list.py
    """

    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)

    print(ll, type(ll))  # pytest输出print()的内容要加 -s参数

    assert len(ll) == 4
    assert ll.find(2) == 2
    assert ll.find(-1) == -1

    assert ll.remove(0) == 1
    assert ll.remove(10) == -1
    assert ll.remove(2) == 1
    assert len(ll) == 2
    assert list(ll) == [1, 3]
    assert ll.find(0) == -1

    ll.appendleft(0)
    assert list(ll) == [0, 1, 3]
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert headvalue == 0
    assert len(ll) == 2
    assert list(ll) == [1, 3]

    assert ll.popleft() == 1
    assert list(ll) == [3]
    ll.popleft()
    assert len(ll) == 0
    assert ll.tailnode is None

    ll.clear()
    assert len(ll) == 0
    assert list(ll) == []


def test_linked_list_remove():
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.remove(7)
    print(list(ll))


def test_single_node():
    # https://github.com/PegasusWang/python_data_structures_and_algorithms/pull/21
    ll = LinkedList()
    ll.append(0)
    ll.remove(0)
    ll.appendleft(1)
    assert list(ll) == [1]


def test_linked_list_reverse():
    ll = LinkedList()
    n = 10
    for i in range(n):
        ll.append(i)
    ll.reverse()
    assert list(ll) == list(reversed(range(n)))


def test_linked_list_append():
    ll = LinkedList()
    ll.appendleft(1)
    ll.append(2)
    assert list(ll) == [1, 2]


if __name__ == '__main__':
    test_single_node()
    test_linked_list()
    test_linked_list_append()
    test_linked_list_reverse()
