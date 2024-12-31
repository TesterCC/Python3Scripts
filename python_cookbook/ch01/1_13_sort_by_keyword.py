# coding=utf-8
'''
DATE: 2020/09/03
AUTHOR: Yanxi Li
'''

"""
1.13 通过某个关键字排序一个字典列表

问题：你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。

解决方案：
通过使用operator模块的itemgetter函数，可以非常容易的排序这样的数据结构。
"""

from operator import itemgetter

rows = [
    {"fname": "Brian", "lname": "Jones", "uid": 1003},
    {"fname": "David", "lname": "Beazley", "uid": 1002},
    {"fname": "John", "lname": "Cleeze", "uid": 1001},
    {"fname": "Big", "lname": "Jones", "uid": 1004},
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(f"rows_by_fname: {rows_by_fname}")

rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(f"rows_by_uid: {rows_by_uid}")


# itemgetter()支持多个keys
print("==== multi-keys ====")
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(f"rows_by_lfname: {rows_by_lfname}")
