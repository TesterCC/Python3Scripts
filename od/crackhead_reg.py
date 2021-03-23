# coding=utf-8
"""
DATE:   2021/3/22
AUTHOR: Yanxi Li
"""
esi = 0x9FCF87AA   # ASCII "12345666"

"""
未完成
"""

buff = "12345666"  # buff中存储serial
flag = 0x0  # 当serial为负数时，flag = 0xFF
i = 0  # buff下标
ecx = 0  # ecx寄存器初始值
edx = 0
m = 3  # 磁盘驱动器类型   int类型
buff_volume_info = "GAME"  # 存储卷标名信息   Sting类型

if buff[i] == "-":  # 判断serial是否为负数
    flag = 0xFF  # 16进制的-1
    i+=1  # 从buff[1]开始

# ecx生成算法
while i < len(buff):
    temp = buff[i] - 30
    ecx += ecx * 4
    ecx = temp + ecx * 2

# eax生成算法
eax = edx + ecx
eax = eax ^ edx  # 异或运算

buff_volume_info.reverse()  # 将卷名信息翻转
# esi生成算法
while m > 0:
    esi += m * buff_volume_info
    m -= 1
esi = esi ^ 0x797a7553

if esi == eax:
    print("success")   # 创建窗口，"Crudd's Crack Head"
else:
    print("fail")