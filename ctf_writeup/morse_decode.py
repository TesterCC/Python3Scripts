#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/3 11:31 
# @Author : MFC

"""
攻防世界 crypto 003 Morse
"""


CODE_TABLE = {
    # 26 个英文字符
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    # 10 个数字
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    # 16 个特殊字符
    ',': '--..--', '.': '.-.-.-', ':': '---...', ';': '-.-.-.',
    '?': '..--..', '=': '-...-', "'": '.----.', '/': '-..-.',
    '!': '-.-.--', '-': '-....-', '_': '..--.-', '(': '-.--.',
    ')': '-.--.-', '$': '...-..-', '&': '. . . .', '@': '.--.-.'

    # custom by yourself
}

def morsedecode(morse):
    msg =''
    codes = morse.split(' ')
    for code in codes:
        if code =='':
            msg += ' '
        else:
            UNCODE =dict(map(lambda t:(t[1],t[0]),CODE_TABLE.items()))
            msg += UNCODE[code]
    return msg

a = open(r'crypto3.txt','r')  # 密文要写入文件中
ciphertext = a.read()

ciphertext = ciphertext.replace('1','-')
ciphertext = ciphertext.replace('0','.')

FLAG = morsedecode(ciphertext)
flag = FLAG.lower()
flag = 'cyberpeace{'+flag+'}'
print('flag is ',flag)