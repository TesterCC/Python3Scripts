# -*- coding: utf-8 -*-
# @Auther: SecCodeCat
# @date  : 2025/11/27

# pip install pwntools -i https://mirrors.aliyun.com/pypi/simple/

from pwn import *

# 不用print也可以输出信息
file = ELF("learn_assembly/helloworld")

print("--"*33)
print(file.section(".text"))
print("--"*33)
print(file.section(".text").hex())
