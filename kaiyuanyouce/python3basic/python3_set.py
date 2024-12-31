# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/11 23:09'

"""
set是Python的基本数据类型，它有可变集合(set()) 和不可变集合(frozenset)两种
其存储的元素是无序的
其存储的元素是不重复
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484022&idx=1&sn=8dc73f60a26dfbff757b05ee87589297&scene=19#wechat_redirect
"""


def basic():
    set1 = set(u"LearnTest PythonTest")
    print(set1)


def crud():
    print(u"set操作示例")

    set_source = set([1, 1, 2, 3, 4, 5, 6, 7])
    set_demo = set([1, 1, 2, 3, 4, 5, 6, 7])

    print(u"原始数据： ", end="")  # 末尾不换行
    print(set_demo)

    # add方法，新增元素
    print(u"add后： ", end="")
    set_demo.add(9)
    set_demo.add(1)
    print(set_demo)

    # remove 删除元素
    print(u"remove后： ", end="")
    set_demo.remove(9)

    print(set_demo)

    # update 新增多个元素值
    list_demo = ["a", "b", "c"]
    set_demo.update(list_demo)

    print(u"update后： ", end="")
    print(set_demo)


def adv():
    s1 = set([1, 2, 3, 4, "a", "b", "c", "d"])
    s2 = set([1, 2, "a", "b"])

    print(u"issubeset演示：")
    print(s1.issubset(s2))   # 判断s1中的每个元素是否都在s2中
    print(s1.issuperset(s2))   # 判断s2中的每个元素是否都在s1中

    print(u"返回两个集合的并集union")
    res1 = s1.union(s2)
    print(res1)

    print(u"返回两个集合的交集intersection")
    res2 = s1.intersection(s2)
    print(res2)

    print(u"s1中有s2中没有的元素:")
    res = s1.difference(s2)
    print(res)


if __name__ == '__main__':
    basic()
    crud()
    adv()
