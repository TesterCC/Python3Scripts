#!/usr/bin/env python
#coding=utf-8

'''
 Python在数据科学中的应用  imooc
 应用matplotlib来进行基本作图
 http://www.imooc.com/video/12986
'''


import matplotlib.pyplot as plt
import matplotlib

print(matplotlib.get_cachedir())

year = [1950,1970,1990,2010]
pop = [2.519, 3.692, 5.263, 6.972]

# plt.plot(year, pop)    #线图
plt.scatter(year, pop)   #散点图
plt.show()    #print picture -- need wait a long time

