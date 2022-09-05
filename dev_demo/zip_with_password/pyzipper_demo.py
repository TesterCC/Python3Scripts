# -*- coding: utf-8 -*-
# @Time    : 2022/9/5
# @Author  : SecCodeCat

# 首先得安装pyzipper库，pip insall pyzipper
import pyzipper
from threading import Thread

"""
Zip加密文件的加密算法通常包括AES和Zip 2.0传统加密(CRC32)算法，针对采用不同加密算法的压缩文件，应采用不同的解密方式进行解密。

本实验用的zip加密文件是通过WinRAR进行创建的，当前WinRAR默认采用AES-256进行加密，WinRAR也可以选择通过Zip 2.0传统加密(CRC32)算法进行加密。

Python标准库中的zipfile模块只支持Zip 2.0传统加密(CRC32)的zip文件，不能解密AES加密的Zip文件；如果要解密AES加密的Zip文件，需要用到pyzipper库。

本文通过zipfile模块来解密Zip 2.0传统加密(CRC32)的zip文件，通过pyzipper库来解密AES加密的Zip文件。

ref：https://www.jianshu.com/p/dd915f27d1f4

"""

def extractFile(zip_file, password):
    with pyzipper.AESZipFile(zip_file, 'r', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as f:
        f.setpassword(password.encode('utf-8'))
        try:
            f.extractall()  # 使用密码尝试解压
            print("[+] Found password: " + password)
        except:
            pass  # 解压失败说明密码错误，跳过


def main():
    # 采用AES默认加密算法的压缩文件
    zip_file_name = "device.zip"
    password = "test123"
    # 启用一个线程去解压，多线程爆破时可以用
    # t = Thread(target=extractFile, args=(zip_file_name, password))
    # t.start()
    extractFile(zip_file_name, password)


if __name__ == '__main__':
    main()
