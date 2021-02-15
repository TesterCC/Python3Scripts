#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/2/15 12:49 
# @Author : MFC

"""
ref: https://www.bilibili.com/video/BV1u5411J7Th
# Q1: 2
# Q2: 6014760148
大数幂取模
欧拉定理：https://zhuanlan.zhihu.com/p/35060143
蒙哥马利算法：https://zhuanlan.zhihu.com/p/35242553
# Q3: 1-2+3*4*5+6*7*8+9
穷举即可
# Q4: in hacking8_v2.py
i.py import aes.py 本地打印看到关键函数 Decrypt2 Hash 和 一段密文
动态flag，根据你做题时获取的密文决定
"""
import base64
import gzip

from multiprocessing import Process
# key = ''
# key[0:10] = 4201353550
# 求key[11:16] = 0 - 999999
# 暴力破解：key = str(4201353550) + key[11:16]
import time

print("Stage 4: ")

from ctf_writeup.hacking8.aes import AESModeOfOperationCTR

def Decrypt2(key: str, text: str) -> str:
    if len(key) < 16:
        key += ' ' * (16 - len(key))
    elif len(key) > 16:
        key = key[0:16]
    aes = AESModeOfOperationCTR(key.encode())
    s = gzip.decompress(aes.decrypt(base64.b64decode(text)))
    print("[DEBUG] ", str(s, encoding='utf-8'))
    return str(s, encoding='utf-8')

def find_key():
    for i in range(100000, 1000000):   # 取了个巧，知道是6位，而且最后一位是6
        key = str(4201353550) + str(i)
        print("[TEST]", key)
        # 需要解密的密文
        c_text = 'ktPSxtF060ZcyAGMC1G38PaEFgga/saD0rANyCWfW6W6fWIqMEDMRNkgv86rCKoai1dzpKiLLuer0LGQtlh5hlXP6ELfrbE7gDX9KyBmpHbiiUEYidT5zasG2fl6okMwBHEhAhkLfuTDA6fEHMk1uDjxK+oGIPGxrO+H3I8bBueQbWNOWRojgRI01IRVDrEMpAOERvAn/I37+8aCBGvH7hoe8XM2gDX6LlQr06oVwY5Nbb+BUYiisdKbmNvPQnpbyS//GRNWkOd7bihAlDsmYaqDRn4V/z2DZMq0yH0b+uh0Dg6/jVLQTTQHmWnvmQ=='
        try:
            ans = Decrypt2(key, c_text)
            print("[DE] ", ans)
            if len(ans) > 0:   # 解密长度大于0时，即解密成功
                print("[+] this is %s" % key)
                break
        except:
            print("wrong key: %s " % key)
            pass

# st = time.time()
# find_key()
# dt = time.time() - st
# print("cost time: ", dt)

if __name__ == '__main__':
    p = Process(target=find_key)
    p.start()
    p.join()