# -*- coding: utf-8 -*-
# @Auther: liyanxi
# @date  : 2026/2/10


from qiling import *
from qiling.const import QL_VERBOSE

def challenge1(ql):
    ql.mem.map(0x1000, 0x1000, info='[challenge1]')
    # 为地址范围?[0x1000, 0x2000) 映射了一块内存，第一个参数0x1000是映射的起始地址，第二个参数0x1000是映射的大小，映射的大小必须是页大小的倍数，这里的页大小是 Qiling模拟器的默认页大小，4096字节。info是对这部分内存做的一个标记，后续Qiling如果想接着使用的话就可以用这个标记来定位。
    ql.mem.write(0x1337, ql.pack16(1337))
    # 将整数值 1337 转换为一个16位字节序列写入内存地址 0x1337 所指定的内存位置，小端输入

if __name__ == '__main__':
    path = ["qilinglab-x86_64"]
    rootfs = "rootfs/x8664_linux"
    # ql = Qiling(path, rootfs)  # demo
    ql = Qiling(path, rootfs, verbose=QL_VERBOSE.OFF, multithread=True)    # debug
    challenge1(ql)
    ql.run()