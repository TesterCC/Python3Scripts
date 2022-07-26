# coding:utf-8

import pyAesCrypt

"""
pip install pyAesCrypt
脚本有一定危险性，建议虚拟机中运行
此为最简demo
"""

# password = "Hacking-to-the-Gate"
# # encrypt
# pyAesCrypt.encryptFile("./test/3.lnk", "./test/3.xxx", password)
# print("[+] finish encrypt...")
# # decrypt
# pyAesCrypt.decryptFile("./test/3.xxx", "./test/d3.lnk", password)
# print("[+] Finish decrypt...")

password = "Hacking-to-the-Gate"
# encrypt
pyAesCrypt.encryptFile("./test/1.txt", "./test/1.xxx", password)
print("[+] finish encrypt...")
# decrypt
pyAesCrypt.decryptFile("./test/1.xxx", "./test/d1.txt", password)
print("[+] Finish decrypt...")
