# coding=utf-8
'''
DATE: 2020/09/07
AUTHOR: Yanxi Li
'''
import hashlib

# 对字符串进行md5加密

host = "10.10.0.1-webapi"

md5 = hashlib.md5()

md5.update(host.encode("utf-8"))

res = md5.hexdigest()

print(res)
