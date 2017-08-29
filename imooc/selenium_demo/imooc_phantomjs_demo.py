#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/8/29 13:24'


# http://www.imooc.com/article/17119

from selenium import webdriver


url = "https://detail.tmall.com/item.htm?spm=a230r.1.14.10.VapbhB&id=541510809037&cm_id=140105335569ed55e27b&abbucket=5&sku_properties=5919063:6536025"

driver = webdriver.PhantomJS()

driver.get(url)

print(driver.page_source)

# 不建议大家直接使用selenium来提取数据， 因为慢！
# 大家可以获取到html之后用lxml来解析数据，lxml是c语言写的，html解析库会快很多。
