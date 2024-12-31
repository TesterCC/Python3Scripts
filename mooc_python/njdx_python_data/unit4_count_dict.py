#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-04 22:59'

from collections import Counter


def countfeq(s):
    s_list = s.split(' ')
    s_list_copy = [item for item in s_list]
    for index, item in enumerate(s_list_copy):
        if '.' in item:
            item = item.replace('.', '')
        if ',' in item:
            item = item.replace(',', '')
        s_list_copy[index] = item
    return Counter(s_list_copy)


if __name__ == "__main__":
    s = "Not clumsy person in this world, only lazy people, only people can not hold out until the last."
    s_dict = countfeq(s.lower())
    word = input()
    print(s_dict[word])