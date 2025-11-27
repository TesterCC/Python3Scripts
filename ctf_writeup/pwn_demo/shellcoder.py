# -*- coding: utf-8 -*-
# @Auther: SecCodeCat
# @date  : 2025/11/27

# 用于获取linux下可执行文件的shellcode

import sys
from pwn import *

context(os="linux", arch="amd64", log_level="error")

file_path = ""
if len(sys.argv) >= 2:
    file_path = sys.argv[1]

# # for test
# if not file_path:
#     file_path = "learn_assembly/helloworld"

file = ELF(file_path)   # 就是命令行传入的第一个参数
shellcode = file.section(".text")
print(shellcode.hex())

# "48be0030400000000000bf01000000ba12000000b8010000000f05b83c000000bf000000000f05"
"""
# method 1
chmod +x shellcoder.py helloworld
./shellcoder.py helloworld

# method 2
python3.12 shellcoder.py helloworld
"""