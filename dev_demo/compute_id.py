# coding=utf-8
"""
DATE:   2021/1/4
AUTHOR: Yanxi Li
"""

import time

_id_count = 0
_id_count_time = int(time.time())

def compute__id():
    global _id_count, _id_count_time
    _id_count += 1
    if time.time() > _id_count_time + 1:
        _id_count = 0
        _id_count_time = int(time.time())
    _id = '{}:{}'.format(_id_count_time, _id_count)

    return _id

if __name__ == '__main__':
    print(compute__id())
    print(compute__id())
    print(compute__id())