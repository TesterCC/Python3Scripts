#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-06 13:48'

user_dict = {}

users = ["lily1", "lily2", "lily3", "lily1", "lily2", "lily2"]

# example 1 -- method 1
# for user in users:
#     if user not in user_dict:
#         user_dict[user] = 1
#     else:
#         user_dict[user] += 1

# example 1 -- method 2
for user in users:
    user_dict.setdefault(user, 0)    # 性能更高，少做一次dict查询
    user_dict[user] += 1

# 统计出现次数
print(f"Test resulte: \n {user_dict}")