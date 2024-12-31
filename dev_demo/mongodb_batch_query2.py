import time
import pymongo

# ref: https://blog.csdn.net/woailyoo0000/article/details/79313349


client = pymongo.MongoClient("mongodb://10.0.0.148:27017/")
db = client["asset"]

asset_col = db["asset"]  # Collection

i = 0

s_time = time.time()

# # method 1
# # total 171908
# for content in asset_col.find({"unknown": True}):
#
#     print(content)
#     i += 1
#
# print(i)
# print(time.time() - s_time)

# 166629
# 4.995682954788208
# 166629
# 4.7673094272613525


for content in asset_col.find({"unknown": True}).batch_size(1000):

    print(content)
    i += 1

print(i)
print(time.time() - s_time)


# 166629
# 4.7773566246032715
# batch 500

# 166629
# 3.6309614181518555
# batch 1000   # 本机合适，再高也快不了多少的样子。

# 166629
# 3.441906452178955
# batch 3000

