# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/17 00:10'


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# 获取下今天的的日期
today = date.today()
print("今天是: %s" % today)

# 把今天的日期年月日分开，重新格式化下一下
print("今天是: %s年%s月%s日 " % (today.year, today.month, today.day))

# 看下今天是星期几
# 星期几    序号
# Monday     0
# Tuesday    1
# Wednesday  2
# Thursday   3
# Friday     4
# Saturday   5
# Sunday     6
# weekday会获取到对应的序号，请根据序号对上上述表，来看是星期几
weekday_num = today.weekday()
print("今天的weekday num是 %s" % weekday_num)

# 输出可读性更好的星期几
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("今天是: %s" % weekdays[weekday_num])
print("-" * 70)

# 输出现在的时间
today_now = datetime.now()
print("现在是 %s" % today_now)

# 用time来构造个时间出来
t = time(hour=12, minute=20, second=30, microsecond=300)
print("我们自己造的时间是 %s" % t)

# 再造个日期时间出来试试
d = datetime(year=2018, month=8, day=8, hour=8, minute=8, second=8)
print("我们自己造是日期时间 %s" % d)

print("-" * 70)

# use timedelta
# timedalte 是datetime中的一个对象，该对象表示两个时间的差值

print("timedelta使用示例：")

now = datetime.now()
next_day = now + timedelta(days=1)   # 增加一天后的时间
next_second = now + timedelta(seconds=1)   # 增加一秒后的时间
span = now - next_day     # 获取时间差对象
print("现在时间：%s" % now)
print("增加一天后的时间：%s" % next_day)
print("增加1s后的时间：%s" % next_second)

# timedelta.total_seconds()方法：返回该时间差 以秒为单位的值
print("以秒为单位获取时间差：%s" % span.total_seconds())


