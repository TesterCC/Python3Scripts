#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-12 16:24'

"""
lesson 3

run in terminal:
cd ~/Python3Demo/pw_python/algorithm
py.test Bag.py 
"""

class Bag:

    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self.__items = list()

    def add(self, item):
        if len(self) > self.maxsize:
            raise Exception('Bag is Full')
        self.__items.append(item)

    def remove(self, item):
        self.__items.remove(item)

    def __len__(self):
        return len(self.__items)

    def __iter__(self):
        for item in self.__items:
            yield item

def test_bag():
    bag = Bag()

    bag.add(1)
    bag.add(2)
    bag.add(3)

    assert len(bag) == 3

    bag.remove(3)
    assert len(bag) == 2

    for i in bag:
        print(i)

if __name__ == '__main__':
    test_bag()
