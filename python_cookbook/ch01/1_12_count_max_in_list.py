# coding=utf-8
'''
DATE: 2020/09/03
AUTHOR: Yanxi Li
'''

"""
1.12 序列中出现次数最多的元素

问题：怎样找出一个序列中出现次数最多的元素

解决方案：
collections.Counter类的most_common()方法
"""

words = ['test', 'look', 'into', 'my', 'eyes', 'look', 'into', 'you', 'understand', 'test', 'look', 'into']

from collections import Counter

word_counts = Counter(words)    # 好好看看Counter的源码

# 找出出现频率最高得3个单词，即词频最高的
top_three = word_counts.most_common(3)
print(top_three)
