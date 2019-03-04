#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/21 13:39'


"""
算法图解  实现图 P85-87  图算法基础   P90 广度优先算法最终代码

广度优先算法
breadth-first algorithm
"""

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", 'jonny']
graph["anuj"] = [""]
graph["peggy"] = [""]
graph["thom"] = [""]
graph["jonny"] = [""]

# key-value添加顺序对应结果无影响，因为散列表是无序的，散列表能将key映射到value
print(graph)

from collections import deque


def person_is_seller(name):
    """
    检查邻居名字是否以m结尾，如果是，则认为此人是芒果销售商
    :param name:
    :return:
    """
    if not name:
        return False

    # return name[-1] == 'm'   # Python2可以，Python3也可以，但写法不优雅
    return name.endswith('m')  # It's better, suggest by Endlex-net


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
    print("\n[+] Start to breadth-first search")

    while search_queue:   # 只要队列不为空
        person = search_queue.popleft()   # 取出其中的第一个人
        if person not in searched:     # 仅当此人未检查时才检查
            if person_is_seller(person):
                print("{} is a mango seller!".format(person))
                return True
            elif person == '':
                print("There is no neighbor...")
            else:
                print("-->", person)
                search_queue += graph[person]
                searched.append(person)    # 将此人加入已检查过的列表
    return False


if __name__ == '__main__':
    search("you")
    search("alice")
    search("thom")



