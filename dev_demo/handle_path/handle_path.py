# -*- coding=utf-8 -*-
import os
dos_path = "C:\\Users\\User\\Documents\\file.txt"
# dos_path = r'C:\Users\Username\Documents\File.txt'
# 将 DOS 路径转换为标准化的 Linux 路径, 主要是处理 \\
linux_path = os.path.normpath(dos_path)

print(f"[D] linux_path: {linux_path}")