# coding=utf-8
"""
DATE:   2021/9/26
AUTHOR: TesterCC
"""
# 压缩多个文件到zip格式-zipfile包实例
# 由于zipfile库必须先生成zip文件再进行下载，所以当生成的zip文件较多且较大时，会逐渐消耗磁盘的容量。为了避免这种情况，我们可以使用zipstream库。

import zipfile
import time


def compress_attaches(files, out_name):
    f = zipfile.ZipFile(out_name, 'w', zipfile.ZIP_DEFLATED)
    for file in files:
        f.write(file)
    f.close()


files = ['10num.py', '10w.py']
compress_attaches(files, f'{int(time.time())}-test.zip')


# 由于zipfile库必须先生成zip文件再进行下载，所以当生成的zip文件较多且较大时，会逐渐消耗磁盘的容量。为了避免这种情况，我们可以使用zipstream库(这个是第三方包)
# pip install zipstream -i https://pypi.tuna.tsinghua.edu.cn/simple
# zipstream可以不生成zip文件，压缩多个文件到zip格式-zipstream包实例

# ref：
# https://blog.csdn.net/xingjingb/article/details/116943162
# https://zhuanlan.zhihu.com/p/342915148
