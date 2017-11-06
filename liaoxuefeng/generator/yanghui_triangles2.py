#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/6 17:46'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000
生成器

杨辉三角定义如下：

          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5   1


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

杨辉三角最本质的特征是，它的两条斜边都是由数字1组成的，而其余的数则是等于它肩上的两个数之和。
"""

# http://www.jianshu.com/p/dbc6e7637d3a
# need understand


def triangles():
    a = [1]
    while True:
        yield a
        # a = [sum(i) for i in zip([0] + a, a + [0])]    # 用zip打包，再用sum求和，何为不用python自带的map,多个循环多难受
        a = list(map(lambda x, y: x + y, [0] + a, a + [0]))


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break