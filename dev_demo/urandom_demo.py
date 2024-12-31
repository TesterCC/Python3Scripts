import os

# https://docs.python.org/zh-cn/3.7/library/os.html?highlight=urandom#os.urandom
# 返回大小为 size 的字符串，它是适合加密使用的随机字节。
# 本函数从系统指定的随机源获取随机字节。对于加密应用程序，返回的数据应有足够的不可预测性，尽管其确切的品质取决于操作系统的实现。
random_bytes_key = os.urandom(32)

print(random_bytes_key)
print(f"type: {type(random_bytes_key)}, length: {len(random_bytes_key)}")