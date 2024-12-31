#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '18/1/8 23:09'

"""
百度杯 CTF比赛 十月场 （这个质量不错）

gmbh{4d850d5c3c2756f67b91cbe8f046eebd}
try to find the flag

write up:
https://www.cnblogs.com/kurokoleung/p/6363845.html


题目：考眼力 类型：misc

密文：gmbh{4d850d5c3c2756f67b91cbe8f046eebd}，从格式上就不难看出是凯撒密码，python脚本如下
     flag，所有字母前移一位,数字不做转换

flag{4c850c5b3b2756e67a91bad8e046ddac}

VprPGS{jnvg_bar_cyhf_1_vf_3?}
tips：flag格式是IceCTF
IceCTF{wait_one_plus_1_is_3?}
"""

# Caesar Cipher

MAX_KEY_SIZE = 26


def getMode():
    while True:
        print('Enter either "encrypt" or "e" or "decrypt" or "d":')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')


def getMessage():
    print('Enter your message:')
    return input()


def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated


mode = getMode()
message = getMessage()
if mode[0] != 'd':
    key = getKey()
print('Your translated text is:')

if mode[0] != 'd':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('decrypt', message, key))