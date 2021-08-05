# coding=utf-8
"""
DATE:   2021/8/5
AUTHOR: TesterCC
"""

# 解析13位时间戳

import time

def parse13timestamp(timestamp):
    # strftime() Convert a time tuple to a string according to a format specification.
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timestamp/1000))

if __name__ == '__main__':
    tl = [1627833756291, 1627919785251]
    for ts in tl:
        print(parse13timestamp(ts))
