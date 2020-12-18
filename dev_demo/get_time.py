# coding=utf-8
"""
DATE:   2020/12/3
AUTHOR: Yanxi Li
DESC: 通过传参计算机时间段，小时省略分秒，日省略小时
"""

import time

def get_time(timestamp, interval='h'):
    timestamp = int(timestamp)
    if timestamp == 0:
        return timestamp

    localtime = time.localtime(timestamp)
    print(localtime)

    if interval == 'h':
        timestamp -= timestamp % 3600  # 减去分和秒

    elif interval == 'd':
        timestamp -= timestamp % 3600
        timestamp -= 3600 * localtime[3]  # 减去小时

    elif interval == 'w':
        timestamp -= timestamp % 3600
        timestamp -= 3600 * localtime[3]
        timestamp -= 3600 * 24 * localtime[6]  # 减去星期

    elif interval == 'm':
        timestamp -= timestamp % 3600
        timestamp -= 3600 * localtime[3]
        timestamp -= 3600 * 24 * (localtime[2] - 1)  # 减去日期

    return timestamp


if __name__ == '__main__':
    print(get_time(1606989020))
    print(get_time(1606989020,interval='d'))
    print(get_time(1606989020,interval='w'))
    print(get_time(1606989020,interval='m'))




