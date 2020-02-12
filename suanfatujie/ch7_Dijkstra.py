#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-02-12 20:21'


"""
算法图解   P108

Dijkstra算法代码实现，题目看书
"""

graph = {}   # 散列表, 将节点的 所有邻居 和 前往邻居 的开销

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

print(graph["start"].keys())

# 然后添加其它节点和邻居

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}   # 终点没有任何邻居



infinity = float("inf")    # 在Python中表示无穷大 inf

# 需要一个散列表来存储每个节点的开销
costs = {}   # 存储每个节点的开销

costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# 还需要一个存储父节点的散列表
parents = {}
parents['a'] = "start"
parents['b'] = "start"
parents['fin'] = None

# 用一个数组，记录处理过的节点，因为对于同一个节点，你不用处理多次。
processed = []

# 找出开销最低的节点
def find_lowest_cost_node(costs):
    # 变量初始化
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:   #  遍历所有节点
        cost = costs[node]
        if cost < lowest_cost and  node not in processed: # 如果当前节点开销更低且未处理过
            lowest_cost = cost     # 就将其视为开销最低的节点
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)  # 在未处理的节点中找出开销最小的节点

while node is not None:  # 此while循环在所有节点都被处理过后结束
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():   # 遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:   # 如果当前节点前往该邻居更近
            costs[n] = new_cost   # 就更新到该邻居的开销
            parents[n] = node     # 同时将该邻居的父节点设置为当前节点
    processed.append(node)        # 将当前节点标记为处理过
    node = find_lowest_cost_node(costs)   # 找出接下来要处理的节点，并循环

print(costs)
print(cost)
