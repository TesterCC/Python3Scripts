#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/2 11:48'

"""
Python GUI编程(Tkinter)
http://www.runoob.com/python/python-gui-tkinter.html

创建一个GUI程序
  1、导入 Tkinter 模块
  2、创建控件
  3、指定这个控件的 master， 即这个控件属于哪一个
  4、告诉 GM(geometry manager) 有一个控件产生了。
"""

from tkinter import *     # 导入 Tkinter 库
root = Tk()    # 创建窗口对象的背景色

# 创建两个列表
list = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']

# 创建两个列表组件
listb = Listbox(root)
listb2 = Listbox(root)

# 第一个小部件插入数据
for item in list:
    listb.insert(0, item)

# 第二个小部件插入数据
for item in movie:
    listb2.insert(0, item)

# 将小部件放置到主窗口中
listb.pack()
listb2.pack()

# 进入消息循环
root.mainloop()
