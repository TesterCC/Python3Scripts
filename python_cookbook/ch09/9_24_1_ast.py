# coding=utf-8
"""
DATE:   2021/8/26
AUTHOR: TesterCC
"""

"""
9.24 解析与分析 Python源码

问题：你想写解析并分析Python源代码的程序。

解决方案：

Python能够计算或执行字符串形式的源代码。
尽管如此，ast模块能被用来将Python源码编译城一个可被分析的抽象语法树（AST）
"""
# Python能够计算或执行字符串形式的源代码。
x = 7
ret1 = eval("0+2*4+x")
print(ret1)

exec('for i in range(7): print(i, end=" ")')


print("print ex:")

import ast

ex = ast.parse('2 + 3*4 + x', mode='eval')

print(ex)

# ast模块能被用来将Python源码编译城一个可被分析的抽象语法树（AST）
print(ast.dump(ex))

print("print top:")
top = ast.parse("for i in range(10): print(i)", mode='exec')
print(top)
print(ast.dump(top))