#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/26 11:10'

"""
最基础的敏感词屏蔽
https://blog.csdn.net/qq_35793358/article/details/77947078
"""

user_input = input("Please input your words: \n")


def filter_sensitive_words(user_text=user_input):
    """
    filter sensitive word in user input text, replace with '*', output '*' and valid words
    :param user_text:
    :return user_text:
    """
    sensitive_words = ('外挂', '傻瓜', '傻逼', '猪', '你妈', 'fuck', 'shit', '傻', '操')  # 实际至少是一个sensitive_words.txt

    if user_text.strip() is None:    # 判断是否是有意义的输入，也可以判断是否为空
        return "Please input meaningful content..."
    else:
        for word in sensitive_words:    # 遍历敏感词汇库
            if word in user_text:       # 判断用户输入的词汇是否有敏感词汇
                _l = len(word)          # 记录该词汇有几个字
                user_text = user_text.replace(word, '*' * _l)   # 将敏感词汇替换成"*"
                return user_text        # 返回处理后内容
        return user_text   # 没有敏感词则直接返回内容


if __name__ == '__main__':
    print(filter_sensitive_words())
