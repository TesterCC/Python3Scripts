#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/3/30 23:18'

"""
3月27日 每日一题

小崔的数学分数从去年的65分提升到了今年的93分，请计算小明成绩提升的百分点，
并用字符串格式化（format）显示出『xx.x%』，只保留小数点后1位
"""


def format_grade(past_score, current_score):
    past_score = past_score
    current_score = current_score
    percentage = current_score/past_score - 1
    improve_percentage = "{:.1%}".format(percentage)
    print(improve_percentage)


if __name__ == '__main__':
    format_grade(93, 65)
    format_grade(65, 93)