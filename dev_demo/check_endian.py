# -*- coding:utf-8 -*-

'''
操作系统中内存都是从小（低）到大（高）排列的，就像看文字一样，从前（左）到后（右），是一个习惯上的行为（规定）。
当数据存储在内存中，由于操作系统环境的不同，对数据的管理/存储方式可能也有所不同，分为大端和小端两种模式，两者区别如下。
（1）小端：低地址存储数据低字节，高地址存储数据高字节，大部分操作系统为小端；（如：CentOS、Ubuntu、Win10）
（2）大端：低地址存储数据高字节，高地址存储数据低字节，存储和显示（人所看到）在数据方向上一致。
'''


def endian_check_v1():
    import sys
    print(f"本机存储模式是 {sys.byteorder.capitalize()} Endian.\n")


def endian_check_v2():
    import struct

    val = 0x12345678
    pk = struct.pack('i', val)
    hex_pk = hex(pk[0])
    if hex_pk == '0x78':
        print('小端')
    elif hex_pk == '0x12':
        print('大端')


if __name__ == '__main__':
    print("检查判断本机操作系统是大端还是小端：")
    endian_check_v1()
    print("===" * 30)
    endian_check_v2()
