#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/4 23:01'


from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://www.baidu.com')

print('over')