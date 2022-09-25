# -*- coding: utf-8 -*-
# @Time    : 2022/9/2
# @Author  : SecCodeCat

# ref: https://mp.weixin.qq.com/s/oAq1CeOxY24yfEcFuPgLaQ

def f_1(L=[]):
    L.append(1)
    print(L)
    print(hex(id(L)))


def f_other_1(B=False):
    print(f"B={B}")
    print(hex(id(B)))


def f_other_2(I=0x41414141):
    print(f"I={I:#x}")
    print(hex(id(I)))


f_1()
f_1()
f_1()       # 前3次调用L地址始终未变
f_1([0])

f_other_1()        # B地址未变
f_other_1(True)
f_other_1()        # B地址未变

print(hex(id(True)))     # 常量True的地址
print(hex(id(False)))    # 常量False的地址

f_other_2()              # I地址未变
f_other_2(0x51201314)
f_other_2()              # I地址未变
