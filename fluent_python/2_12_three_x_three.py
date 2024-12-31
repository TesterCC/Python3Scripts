# coding=utf-8
'''
DATE: 2020/09/03
AUTHOR: Yanxi Li
'''

# 2-12 包含3个列表的列表， 嵌套的 3 个列表各自有 3 个元素来代表井字游戏的一行方块

board = [['_']*3 for i in range(3)]

print(board)

# 第1行第2列元素标记为X
board[1][2] = 'X'

print(board)