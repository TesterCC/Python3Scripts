#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-07 10:16'

from hashids import Hashids

# pip install hashids
# 自定义的字母表中的字符至少应含有16个字符。
ALPHABET = 'abcdefghijklmnopqrstuvwxyz1234567890'
ALPHABET2 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
hashids = Hashids(salt="hdj_expo_url", min_length=10, alphabet=ALPHABET)


def encode_expo_id(expo_id):
    encode_expo_id = hashids.encode(expo_id)
    print(encode_expo_id)


def decode_expo_id(encode_expo_id):
    expo_id = hashids.decode(encode_expo_id)
    print(expo_id[0])


if __name__ == '__main__':
    for i in range(1, 11):
        encode_expo_id(i)

    decode_expo_id("4qz3mv3vo1")
    decode_expo_id("7vw3gx819l")
