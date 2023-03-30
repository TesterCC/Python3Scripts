# -*- coding=utf-8 -*-

import datetime
import time


def convert_to_utc(timestamp):
    return int(datetime.datetime.utcfromtimestamp(timestamp).timestamp())


def local13toutc10(timestamp):
    ts = timestamp / 1000
    return int(datetime.datetime.utcfromtimestamp(ts).timestamp())


if __name__ == '__main__':
    # ts = time.time()
    # print(ts)
    # utc_time = convert_to_utc(ts)
    # print(utc_time)
    # print(f"delta: {int(ts-utc_time)}")

    print("样例时间：2023-04-08 23:59:59")
    ts = 1680278399999
    print(f"系统13位本地时间戳：{ts}")
    print(f"载荷10位UTC时间戳：{local13toutc10(ts)}")

    # print(int(ts/1000)-local13toutc10(ts))   # 28800