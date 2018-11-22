#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/21 13:39'


"""
算法图解  实现图 P85-87  图算法基础   P90 广度优先算法最终代码
"""

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]    # tom is mango
graph["anuj"] = [""]
graph["peggy"] = [""]
graph["thom"] = [""]
graph["jonny"] = [""]

print(graph)    # 散列表是无序的，散列表能将key映射到value

from collections import deque


def person_is_seller(name):
    """
    检查邻居名字是否以m结尾，如果是，则认为此人是芒果销售商
    :param name:
    :return:
    """
    if not name:
        return False

    return name[-1] == 'm'   # Python2可以，Python3报错


def search(name):

    """
    广度优先搜索
    :param name:
    :return:
    """

    search_queue = deque()

    search_queue += graph[name]

    searched = []

    # print(search_queue)

    while search_queue:   # 只要队列不为空
        person = search_queue.popleft()   # 取出其中的第一个人
        if person not in searched:     # 仅当此人未检查时才检查
            if person_is_seller(person):
                print("{} is a mango seller!".format(person))
                return True
            else:
                print("-->", person)
                search_queue += graph[person]
                searched.append(person)    # 将此人加入已检查过的列表
    return False


if __name__ == '__main__':
    search("you")
    # print(search("alice"))
    # print(search_target("thom"))   # 引起各种问题



