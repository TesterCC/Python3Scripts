# coding=utf-8
"""
DATE:   2022/3/17
AUTHOR: TesterCC
"""

import time
import uuid

def gen_multi_uuid(count=10):
    for i in range(0,count):
        print(uuid.uuid4())
        time.sleep(0.1)

if __name__ == '__main__':
    gen_multi_uuid(9)
