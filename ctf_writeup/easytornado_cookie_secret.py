# coding=utf-8
"""
DATE:   2021/3/19
AUTHOR: Yanxi Li
"""

"""
攻防世界 Web高级
016 easytornado

护网杯 2018的题
"""

import hashlib

def compute_md5(data):
    md5 = hashlib.md5()
    md5.update(data.encode('utf-8'))  # 必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
    return md5.hexdigest()

def get_filehash(cookie_secret):
    # md5(cookie_secret+md5(filename))
    filename = '/fllllllllllllag'
    filehash = compute_md5(cookie_secret+compute_md5(filename))
    return filehash

if __name__ == '__main__':
    print(get_filehash("2c2fb315-e84d-4865-beab-d6047bce4d01"))