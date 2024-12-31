#!/usr/bin/env python
#coding=utf-8

'''
 Python在数据科学中的应用  imooc
 http://www.imooc.com/video/12988
 个性化
'''


import matplotlib.pyplot as plt

population = [1.0, 1.262, 1.650]+[2.519, 3.692, 5.263, 6.972]
year = [1800,1850,1900]+[1950,1970,1990,2010]

# plt.plot(year, population)   # 设置线图
plt.fill_between(year, population, 0, color='green')   #生成填充图

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projects')
plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B','8B','10B'])

plt.show()