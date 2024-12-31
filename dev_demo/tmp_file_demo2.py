# -*- coding: utf-8 -*-
# @Time    : 2022/8/28
# @Author  : SecCodeCat

# 创建临时文件
import tempfile

'''
http://t.zoukankan.com/liuhui0308-p-12464003.html
https://blog.csdn.net/weixin_37926734/article/details/123563067
https://docs.python.org/zh-tw/dev/library/tempfile.html
'''

# fp = tempfile.TemporaryFile()
# print(fp.name)
# fp.write('两情若是久长时，'.encode('utf-8'))
# fp.write('又岂在朝朝暮暮。'.encode('utf-8'))
# # 将文件指针移到开始处，准备读取文件
# fp.seek(0)
# print(fp.read().decode('utf-8')) # 输出刚才写入的内容
# # 关闭文件，该文件将会被自动删除
# fp.close()

# 通过with语句创建临时文件，with会自动关闭临时文件
# with tempfile.TemporaryFile() as fp:
with tempfile.NamedTemporaryFile() as fp:
    # 写入内容
    fp.write(b'I Love Security, Python and Go!')
    # 将文件指针移到开始处，准备读取文件
    fp.seek(0)
    # 读取文件内容
    print(fp.read()) # b'I Love Python!'
    print("temp file name: ", fp.name)

# 通过with语句创建临时目录
with tempfile.TemporaryDirectory() as tmpdirname:
    print('创建临时目录', tmpdirname)
