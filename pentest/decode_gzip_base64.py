# coding=utf-8
"""
DATE:   2021/6/2
AUTHOR: Yanxi Li
"""

import base64
import gzip
from io import BytesIO
from io import StringIO

# 有人问密文是什么加密，有人注意到是 gzip + base64 , 貌似是python2的

def de_ciper():
    print(gzip_uncompress(base64.b64decode(
        "H4sIAAmhtGAA/2NgZGBg+A8EIBoEWEAMvuDK4pLUXD2n/Pyc1MQ8kBB7bnxZYk5pKgMjIzcAmxcDozUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==")))


def gzip_uncompress(c_data):
    try:
        buf = BytesIO(c_data)
        print(gzip.GzipFile(mode='rb', fileobj=buf).read())
    except Exception as  e:
        print("uncompress wrong" + e)


# de_ciper()

if __name__ == '__main__':

    txt = de_ciper()
    print(txt)
