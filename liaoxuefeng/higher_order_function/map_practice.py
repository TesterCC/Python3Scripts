#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/7 21:58'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，
输出：['Adam', 'Lisa', 'Bart']
"""

L1 = ['adam', 'LISA', 'barT']


def normalize(name):
    return name.capitalize()

# capitalize() 与 title() 都是可以使字符串首字母大写
# title() 作用于整个字符串内的单词的首字母大写   --> 'This Is A Test String'
# capitalize() 则只有整个字符串的第一个字母大写  --> 'This is a test string'


if __name__ == '__main__':
    L2 = list(map(normalize, L1))
    print(L2)

