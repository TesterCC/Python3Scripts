# coding=utf-8
"""
DATE:   2021/1/4
AUTHOR: Yanxi Li
"""

import time

_id_count = 0
_id_count_time = int(time.time())

# 顺序不同会引起_id_count初始值的问题
def compute__id():

    global _id_count, _id_count_time

    _id_count += 1

    _id = '{}:{}'.format(_id_count_time, _id_count)

    if time.time() > _id_count_time + 1:
        _id_count = 0
        _id_count_time = int(time.time())

    return _id

## 错误示例，仅供对比
# def compute__id_error():
#
#     global _id_count, _id_count_time
#
#     _id_count += 1
#
#     if time.time() > _id_count_time + 1:
#         _id_count = 0
#         _id_count_time = int(time.time())
#
#     _id = '{}:{}'.format(_id_count_time, _id_count)
#
#     return _id


if __name__ == '__main__':
    for i in range(10):
        print(compute__id())
        # print(compute__id_error())
        time.sleep(0.3)
