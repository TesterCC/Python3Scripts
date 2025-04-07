import re


"""
反转句子里的单词，比如"Hello, Go language"，翻转为"language Go Hello"，单词间不一定用空格间隔。
这个题用python如何解答
"""

def reverse_words(sentence):
    # 使用正则表达式来分割句子，匹配非字母数字字符作为分隔符
    words = re.split(r'[^a-zA-Z0-9]+', sentence)
    # words = re.split(r'[^a-zA-Z0-9,]+', sentence)
    # 过滤掉空字符串
    words = [word for word in words if word]
    # 反转单词列表, 间隔符也可以换成其它的
    reversed_words = ' '.join(reversed(words))
    return reversed_words


# 测试示例
sentence = "Hello, Go language"
print(reverse_words(sentence))
