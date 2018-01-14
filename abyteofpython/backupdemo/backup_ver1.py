#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/14 17:09'

import os
import time


# 1.需要备份的文件与目录被指定在一个列表中。
# 例如：windows下：
# source=['C:\\My Documents', 'C:\\Code']
# 又如在Mac OS X与Unix下:
# source=['/Users/TesterCC/test']
# 注意: 这里必须在字符串中使用双引号，用以括起其中包含空格的名称

source = ['/Users/TesterCC/test']

# 2.备份文件必须存储在一个主备份目录中
target_dir = '/Users/TesterCC/backup'

# 3.备份文件将打包至zip文件
# 4.zip压缩文件的文件名由当前日期与时间构成
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 5.使用zip命令嫁给你文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(target, ''.join(source))


# 6.运行备份
print('Zip command is:')
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED, please confirm it.')

