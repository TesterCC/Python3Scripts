# coding=utf-8
"""
DATE:   2022/5/30
AUTHOR: TesterCC
"""
# coding:utf-8

import uuid

# 注意 {{ 可以打印 {
def gen_flags(count=7):
    print(f"Generate {count} flag(s)...")
    for i in range(count):
        print("flag{{{}}}".format(uuid.uuid4()))


if __name__ == '__main__':
    gen_flags(10)
