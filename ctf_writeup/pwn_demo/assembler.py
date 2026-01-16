# -*- coding: utf-8 -*-
# @Auther: SecCodeCat
# @date  : 2026/1/7

# 核心功能是将一段十六进制字符串(shellcode)转换并保存为一个可执行的Linux ELF文件
import sys, os, stat
from pwn import *

context(os="linux", arch="amd64", log_level="error")

ELF.from_bytes(unhex(sys.argv[1])).save(sys.argv[2])
os.chmod(sys.argv[2], stat.S_IEXEC)
