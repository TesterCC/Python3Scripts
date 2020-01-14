#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-01-14 15:51'

"""
4-1 Python内置数据结构算法常考

什么是LRUCache？

Least-Recently-Used 替换掉最近最少使用的对象

1.缓存剔除策略，当缓存空间不够用的时候需要一种方式剔除key

2.常见的有：LRU(Least-Recently-Used,替换掉最近最少使用的对象)，LFU(Least-Frequently-Used,根据数据的历史访问频率来淘汰数据) 

3.LRU通过使用一个循环双端队列不断把最新访问的key放到表头、把最远的访问放到最后、把最远访问的key剔除即可。

重点：如何实现LRUCache？

字典用来缓存，循环双端链表用来记录访问顺序

1)利用Python内置的dict+collections.OrderedDict实现
2)dict用来当作k/v键值对的缓存
3)OrderedDict用来实现更新最近访问的key

要求：
自己实现LRUCache，并编写单元测试
"""

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity=128):
        # capacity表示最多有多少个key
        self.od = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.od:
            val = self.od[key]
            self.od.move_to_end(key)   # 每次访问更新最新使用的key，把最近访问的放到最右边，表示最新
            return val
        else:
            return -1

    def put(self, key, value):
        """更新key/value值
        分2种情况:
        1.如果key在od里，需要把它删除，然后重新赋值
        2.判断当前容量capacity是否已经满了，如果满了，则把最早的一个key给删除
        """
        if key in self.od:
            del self.od[key]
            self.od[key] = value   # 更新key到表头，最右边
        else: # insert
            self.od[key] = value
            # 判断当前容量capacity是否已经满了
            if len(self.od) > self.capacity:
                self.od.popitem(last=False) # 把最早的一个key给删除

# 自己实现LRUCache，并编写单元测试






