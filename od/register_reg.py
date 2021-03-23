# coding=utf-8
"""
DATE:   2021/3/19
AUTHOR: Yanxi Li
"""


def reg(usrname):
    username_length = len(usrname)
    esi = 0
    for i in range(username_length):
        eax = ord(usrname[i])
        if eax != 32:
            eax = eax * 4
            esi = eax + esi
    ebx = 0x654789
    print("%x" % ebx)
    for i in range(username_length):
        ebx = ebx - 1
        ebx += ebx * 2 - 1
    print("%x" % ebx)
    ebx = 0xFFFFFFFF & ebx  # 只取ebx的后面八位
    print('BS-%08X-%d' % (ebx, esi))


while (1):
    usrname = input("input usrname:")
    reg(usrname)