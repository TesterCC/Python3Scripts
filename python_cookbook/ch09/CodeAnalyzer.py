# coding=utf-8
"""
DATE:   2021/9/17
AUTHOR: TesterCC
"""

"""
9-24 P364  分析源码树需要你自己更多的学习，它是由一系列AST节点组成的。
分析这些节点最简单的方法就是定义一个访问者类，实现很多visit_NodeName()方法，NodeName()匹配哪些你感兴趣的节点。
例子的类，记录了哪些名字被加载、存储和删除的信息。
"""

import ast

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()

    def visit_Name(self, node):
        pass