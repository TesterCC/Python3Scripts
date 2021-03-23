# coding=utf-8
"""
DATE:   2021/3/22
AUTHOR: Yanxi Li
"""

"""
ref:
https://bbs.pediy.com/thread-21378.htm

crackhead程序的注册机算法：
前面我们已经说了取磁盘类型参数做循环次数，再取卷标值 ASCII 码的逆序作为数值，有了这两个值就开始计算了。
现在我们把磁盘类型值作为 n，卷标值 ASCII 码的逆序数值作为 a，最后得出的结果作为 b。
这里算出来的 b 最后还要和 797A7553H 异或一下才是真正的注册码。
"""

n = 3  # 磁盘驱动器类型   int类型  0x03，OD直接获取的，应该有win32api可以调用获取才对

iKey = 0   # 卷标值 ASCII 码的逆序数值
iSum = 0   # 计算结果，即注册码

# Key值只占用1个寄存器大小，四个节
# 寄存器里字节存放次序与内存存放次序相反，所以倒过来
# 每向高处移动一字节（8位），需要乘2 ^ 8

# iKey = 0x47414D45
# iKey = 0x454D4147  # 卷标GAME OK, 直接转应该是47 41 4D 45 ， 这里应该计算出来。 GAME  ebx 454D4147， 数据面板   47414D45
# iKey = 0x74736574  # 卷标test, 直接转应该是 74 65 73 74
# iKey = 0           # 没有卷标


iKey = 0x74736574   # 卷标test逆序

for i in range(n):
    iSum += (n-i)*iKey

# print(iSum)
iSum ^= 0x797a7553

print("Key: ", iSum)
