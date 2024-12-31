# coding=utf-8
"""
DATE:   2020/11/24
AUTHOR: Yanxi Li
"""

import pymongo
import time
from threading import Thread

# set custom _id 多进程 todo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client["test_custom"]

test_col = db["custom_id"]  # Collection

_id_count = 0  # 用于处理并发
_id_count_time = int(time.time())


def insert_custom_id():
    global _id_count, _id_count_time

    # 处理并发的操作
    _id_count += 1
    if time.time() > _id_count_time + 1:
        _id_count = 0
        _id_count_time = int(time.time())

    custom__id = "{}:{}".format(_id_count_time, _id_count)

    # _id_count = test_col.find({'_id': custom__id}).count()   # old pymongo use
    # _id_count2 = test_col.count_documents({'_id': custom__id})   # new pymongo use

    print(custom__id)
    test_col.insert_one({'_id': custom__id})


def multi_threading_query(count=10):
    # 多线程主
    # 创建 新增自定义_id 线程
    url_thread = Thread(target=insert_custom_id())
    # 详情线程组
    detail_thread = []

    for i in range(count):
        thread2 = Thread(target=insert_custom_id())
        detail_thread.append(thread2)

    print("detail_thread: ", len(detail_thread))

    # 开启url线程
    url_thread.start()

    for i in range(count):
        # 开启详情进程
        detail_thread[i].start()

    # 等待所有子进程结束
    url_thread.join()
    for i in range(count):
        detail_thread[i].join()

    print("total insert count: {}".format(count))


if __name__ == '__main__':
    # check_custom_id()
    # 写个多线程/多进程脚本测试下
    # insert count 主线程+子线程
    # 要提高效率，不要用多线程，而是要用多进程
    multi_threading_query(count=300)
