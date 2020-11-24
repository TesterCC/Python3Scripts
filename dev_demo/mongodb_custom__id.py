# coding=utf-8
"""
DATE:   2020/11/24
AUTHOR: Yanxi Li
"""

import pymongo
import time

# set custom _id

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client["test_custom"]

test_col = db["custom_id"]  # Collection


def check_custom_id():
    global global_count
    current_time = int(time.time())


    custom__id = "{}:{}".format(current_time, 0)


    _id_count = test_col.find({'_id': custom__id}).count()   # old pymongo use
    print(_id_count)
    # _id_count2 = test_col.count_documents({'_id': custom__id})   # new pymongo use
    # print(_id_count2)
    if _id_count > 0:
        custom__id = "{}:{}".format(current_time, _id_count)

    print(custom__id)


if __name__ == '__main__':
    check_custom_id()

