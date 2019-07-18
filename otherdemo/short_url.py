#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-16 17:46'

import os
import requests
import json
from tkinter import *


class Get_url_short():
    def __init__(self):
        self.source = 2540340328    # 2540340328, 2849184197, 202088835, 211160679
        self.url = 'https://api.t.sina.com.cn/short_url/shorten.json?'

    def get_short(self):
        try:
            url_long = self.tk_url_long.get()
            url = self.url + 'source=' + str(self.source) + '&url_long=' + str(url_long)
            html = requests.get(url)
            html = html.text
            html = json.loads(html)
            self.url_short = html[0]['url_short']
            Label(text='Short URL:').grid(row=1, column=0)
            Label(text=self.url_short).grid(row=1, column=1)
            Button(self.short, text="Copy", width=10, command=self.short_copy).grid(row=1, column=2, sticky=W, padx=10,
                                                                                    pady=5)
        except:
            Label(text='请输入带http或https的长链接').grid(row=2, column=1)

    def short_copy(self):
        try:
            self.short.clipboard_clear()  # 清除剪贴板内容
            self.short.clipboard_append(self.url_short)  # 向剪贴板追加内容
            Label(text='URL copy succeeded', font=', 10').grid(row=2, column=1)
        except:
            Label(text='URL copy failed', font=', 10').grid(row=2, column=1)

    def short_begin(self):
        self.short = Tk()
        self.short.title('Short URL')
        Label(text='Long URL：').grid(row=0, column=0)
        self.tk_url_long = Entry(self.short)
        self.tk_url_long.grid(row=0, column=1)
        Button(self.short, text="转化", width=10, command=self.get_short).grid(row=0, column=2, sticky=W, padx=10, pady=5)
        mainloop()


# from other, no use in the script now

def sina_url(api, source, url_long):
    url = api + 'source=' + str(source) + '&url_long=' + str(url_long)
    http = requests.get(url)
    jsonstr = json.loads(http.text)
    url_short = jsonstr[0]['url_short']
    copy(url_short)


def copy(url_short):
    os.system('echo ' + url_short + '| clip')

if __name__ == '__main__':
    short = Get_url_short()
    short.short_begin()