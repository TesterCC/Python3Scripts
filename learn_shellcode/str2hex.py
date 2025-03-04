# -*- coding:utf-8 -*-
# shellcode basic
# python3实现字符串转ascii码, 再转成hex
# go demo: str2hex.go
s = "/bin/sh"

# ['0x2f', '0x62', '0x69', '0x6e', '0x2f', '0x73', '0x68']

# ASCII（美国信息交换标准代码）是一套基于拉丁字母的字符编码系统，它使用 7 位二进制数表示 128 个字符，范围从 0 到 127，主要用于表示英文字母、数字、标点符号等。
# Unicode 涵盖了 ASCII，所以 ASCII只是Unicode的一个子集
# ord(char) 函数用于获取单个字符的 ASCII 值，注意：当使用ord()函数处理 ASCII范围（即 U+0000 到 U+007F 范围）内的字符时，返回的 Unicode 码点与 ASCII 码值是相同的。
# 1.获取ASCII值
ascii_values = [ord(char) for char in s]
print("1.ascii value:")
print(ascii_values)

# 2.转换为十六进制
# hex(value) 函数将整数转换为十六进制字符串形式。遍历后将每个 ASCII 值转换为十六进制字符串。
hex_values = [hex(value) for value in ascii_values]
print("2.hex value:")
print(hex_values)

# 3.hex value 字符串还原
# 转换为字符
# 遍历 hex_list 中的每个十六进制字符串。int(h, 16) 将十六进制字符串转换为对应的十进制整数，chr() 函数再将这个十进制整数转换为对应的字符，生成包含转换后字符的列表 chars。
chars = [chr(int(h, 16)) for h in hex_values]
# 拼接字符串
original_str = ''.join(chars)
print("3.restore string:")
print(original_str)