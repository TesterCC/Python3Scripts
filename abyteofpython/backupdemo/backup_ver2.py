#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/25 20:08'

"""
A-Byte-of-Python   P91 
Maintenance 维护阶段
1.优化命名机制--使用时间作为文件名，存储在以当前日期为名字的文件夹中，该文件夹照常存储在主备份目录。
2.优点：
  文件备份会以分层的形式予以存储，更易于管理
  文件名更短
  由于只有当天进行了备份才会创建相应目录，独立的目录能够帮助你快速地检查每天是否都进行了备份。                                                                                                                                                                                                                                                                                                       
"""

import os
import time


# 1.需要备份的文件与目录被指定在一个列表中。
# 例如：windows下：
# source=['C:\\My Documents', 'C:\\Code']
# 又如在Mac OS X与Unix下:
# source=['/Users/TesterCC/test']
# 注意: 这里必须在字符串中使用双引号，用以括起其中包含空格的名称

source = ['/Users/TesterCC/test']    # 要备份的文件所在的目录

# 2.备份文件必须存储在一个主备份目录中
# 例如在Windows下:
# target_dir = "E:\\Backup"
# 又例如在Mac OS X和Linux下:
target_dir = '/Users/TesterCC/backup'   # 要记得将此处目录地址修改至你将使用的路径

# 如果目标目录不存在则创建目录
if not os.path.exists(target_dir):
    os.mkdir(target_dir)   # create directory

# 3.备份文件将打包压缩成zip文件
# 4.将当前日期作为主备份目录下的子目录名称
today = target_dir + os.sep + time.strftime("%Y%m%d")     # os.sep 更改操作系统中的路径分隔符，如'/'

# 将当前时间作为zip文件的文件名
now = time.strftime('%H%M%S')

# zip文件名称格式
target = today + os.sep + now + '.zip'

# 如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5.使用zip命令将文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(target, ''.join(source))


# 6.运行备份
print('Zip command is:')
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED, please confirm it.')


