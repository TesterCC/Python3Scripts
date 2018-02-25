#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/25 20:54'


"""
A-Byte-of-Python  P97
继续改进
需求：
1.支持参数设置
  在程序中添加-v显示详尽程序
  在程序中添加-q使程序能静默运行
  在程序中添加-V显示程序版本号
2.在命令行中允许额外的文件与目录传递到脚本中
  从sys.argv获得名称
  通过list类的extend方法把名称添加到source列表中
3.不使用os.system创建备份
  使用zipfile和tarfile来归档文件

软件开发流程中的阶段(Phases)
1. What       分析
2. How        设计
3. Do It      执行
4. Test       测试与修复错误
5. Use        操作或开发
6. Maintain   维护改进
"""

