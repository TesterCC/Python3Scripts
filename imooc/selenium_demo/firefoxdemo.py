#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/8/29 13:31'


# http://www.imooc.com/article/17119

from selenium import webdriver

url = "https://detail.tmall.com/item.htm?spm=a230r.1.14.10.VapbhB&id=541510809037&cm_id=140105335569ed55e27b&abbucket=5&sku_properties=5919063:6536025"
# url = "http://www.imooc.com/article/17119"

driver = webdriver.Firefox()
# driver = webdriver.Firefox(executable_path='C:/xxx/Downloads/geckodriver-v0.15.0-win64/geckodriver.exe')  # if don't config browser driver path

driver.get(url)

print(driver.page_source)