# -*- coding: utf-8 -*-
# @date  : 2025/12/10
import os
import tempfile
import time

scan_target = r"D:\ws_python\Python3Scripts\dev_demo\tempfile_demo\files"

"""
把tokei.toml写到 /root/.config 目录下可以全局生效。
而且这样就不用担心 /root/.config/tokei.toml 干扰其它指定目录的文件检测了。

ref:
https://github.com/XAMPPRocky/tokei/issues/944
"""


# 在try块之前创建临时文件

# with tempfile.NamedTemporaryFile(mode='w', suffix='.toml', dir=scan_target) as f:
# with tempfile.NamedTemporaryFile(mode='w', suffix='.toml', dir=scan_target, delete=False) as f:

# 默认执行完这个文件就删除了，除非指定delete=False
with tempfile.NamedTemporaryFile(mode='w', suffix='.toml', dir=scan_target, delete=False) as f:
    f.write('treat_doc_strings_as_comments = true\n')
    tokei_config_path = f.name
    tokei_config_filename = os.path.basename(tokei_config_path)
    print(f"temp file path: {f.name}")
    print(f"temp file name: {tokei_config_filename}")

print("mock run task...")

os.remove(tokei_config_path)
