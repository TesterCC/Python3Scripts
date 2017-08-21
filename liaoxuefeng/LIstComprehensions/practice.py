#!/usr/bin/env python
# coding:utf-8

# 列表生成式
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431779637539089fd627094a43a8a7c77e6102e3a811000


'''
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
使用内建的isinstance函数可以判断一个变量是不是字符串
请修改列表生成式，通过添加if语句保证列表生成式能正确地执行
L1 = ['Hello', 'World', 18, 'Apple', None]
期待输出: ['hello', 'world', 'apple']
'''

L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s, str)]   # recommend
# L3 = [s.lower() for s in L if isinstance(s, str) != False]     # not recommand
L3 = [s.lower() for s in L if isinstance(s, str) is not False]  # PEP-8 standard

print(L2)
print(L3)

