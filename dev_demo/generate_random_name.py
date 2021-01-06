# coding=utf-8
"""
DATE:   2021/1/5
AUTHOR: Yanxi Li
"""

import os
import uuid

def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename

if __name__ == '__main__':
    ret = random_filename("d://test/test.jpg")
    print(ret)

