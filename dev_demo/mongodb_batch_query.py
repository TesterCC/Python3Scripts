import time
import pymongo

# ref: https://blog.csdn.net/woailyoo0000/article/details/79313349


client = pymongo.MongoClient("mongodb://10.0.0.148:27017/")
db = client["asset"]

asset_col = db["asset"]  # Collection

i = 0

s_time = time.time()
# total 171908
for content in asset_col.find():  # 1.8085236549377441

    i += 1

print(i)
print(time.time() - s_time)

j = 0

s_time = time.time()
# total 171908  # 针对cursor超时常用
for content in asset_col.find().batch_size(500):
    j += 1

print(j)
print(time.time() - s_time)
