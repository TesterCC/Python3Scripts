# coding=utf-8
"""
DATE:   2021/7/26
AUTHOR: TesterCC
"""

import hashlib

def gen_hash256_id(text:str):
    x = hashlib.sha256()
    x.update(text.encode())
    return x.hexdigest().upper()

if __name__ == '__main__':
    ret = gen_hash256_id("xxx漏洞")
    print(ret)