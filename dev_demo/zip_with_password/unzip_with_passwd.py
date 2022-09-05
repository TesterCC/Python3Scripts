# coding:utf-8

import pyminizip
# pyminizip仅支持传统zip加密，要支持winrar默认的aes加密，需要使用pyzipper
# linux
pwd = "test123"
pyminizip.uncompress("test2.zip", pwd, "./", 1)  # 最后一个参数 int(withoutpath)