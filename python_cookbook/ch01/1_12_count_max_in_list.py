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

from collections import Counter

words = ['look','into','my','eyes','test', 'look', 'my', 'why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes',"your're", "under"]

# Counter对象可以接受任意hashable元素构成的序列对象为输入
# 在底层实现上，一个Coutner对象就是一个字典，将元素映射到它出现的次数上
word_counts = Counter(words)  # 好好看看Counter的源码

# 找出出现频率最高得3个单词，即词频最高的
top_three = word_counts.most_common(3)
print(top_three)

print(word_counts['not'])
print(word_counts['eyes'])

print("====manual count====")
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

# manual count
# method 1
# for word in morewords:
#     word_counts[word] += 1

# method 2
word_counts.update(morewords)

print(word_counts['eyes'])


# Counter实例鲜为人知的特性：可以很容易的跟数学运算操作相结合。
# 制表或统计数据场景适用

print("====demo3 count Counter====")
a = Counter(words)
b = Counter(morewords)

print(a)
print(b)

c = a+b
print(c)

d = a-b
print(d)