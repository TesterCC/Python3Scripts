# -*- coding: utf-8 -*-
# @Auther: liyanxi
# @date  : 2025/11/28

import sys
from pwn import *

# shellcode_str = "4831db66bb79215348bb422041636164656d5348bb48656c6c6f204854534889e64831c0b0014831ff40b7014831d2b2120f054831c0043c4030ff0f05"

context(os="linux", arch="amd64", log_level="error")  # run in linux x86_64

run_shellcode(unhex(sys.argv[1])).interactive()