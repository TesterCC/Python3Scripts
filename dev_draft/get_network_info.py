#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-15 16:49'


"""
如何用python取得Chrome Dev Tools Network面板中的Summary数据？
https://segmentfault.com/q/1010000016638612/a-1020000016639406
"""


from selenium import webdriver
import pprint

driver = webdriver.Chrome()
try:

    driver.get("https://www.imooc.com")
    performance_data = driver.execute_script("return window.performance.getEntries();")
    # print(type(performance_data))
    # pprint.pprint(performance_data)
    for item in performance_data:
        print(item.get('name'))    # 要正则匹配http开头的资源, name里不一定都是url

    print("*"*90)



    # all return None
    # navigationStart = driver.execute_script("return window.PerformanceTiming.navigationStart")
    # responseEnd = driver.execute_script("return window.PerformanceTiming.responseEnd")
    # loadEventEnd = driver.execute_script("return window.PerformanceTiming.loadEventEnd")

    # backendPerformance = responseEnd - navigationStart
    # frontendPerformance = loadEventEnd - responseEnd
    # FinisheTime = backendPerformance + frontendPerformance

except Exception as err:
    print(err)
finally:
    driver.quit()