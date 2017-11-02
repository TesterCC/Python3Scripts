#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/2 11:17'

"""
图形界面
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143200341926302f99cf6f6414dca9dfaaf6e5a25a5b1000
"""

from tkinter import *    # 导入Tkinter包的所有内容


# Step 1 从Frame派生一个Application类，这是所有Widget的父容器
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

# Step 2 在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget
    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world! - by TesterCC')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

# Step 3 第三步，实例化Application，并启动消息循环
app = Application()
# 设置窗口标题:
app.master.title('Hello TK!')
# 主消息循环:
app.mainloop()