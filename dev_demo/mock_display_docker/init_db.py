# -*- coding: utf-8 -*-
import traceback

import pymongo

db_name = "i_cm"
db_host = "127.0.0.1"
db_port = "27017"

col_name_list = ["audit", "counters", "device_info", "task", "pm_device_info"]

try:
    print(f'[*] Initialize {db_name} database ...')
    mongo_client = pymongo.MongoClient(f'mongodb://{db_host}:{db_port}')
    db = mongo_client[db_name]

    for col_name in col_name_list:
        db_col = db[col_name]
        db_col.drop()
        db.create_collection(col_name)  # create collection

    print("[*] Clear all old collections ...")

    # 注意counters作为计数器需要存在，初始化需要，task_id自增需要
    counters_col = db['counters']
    counters_col.insert_one({"_id": "task_id", "sequence_value": int(0)})

    print(f"[*] Finish {db_name} initialization ...")

except:
    traceback.print_exc()
