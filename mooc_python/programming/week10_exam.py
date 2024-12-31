#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-11 09:35'

# task1
s=input()
r = s.replace(" ","")
print(r)


# task2
with open("latex.log") as f:
    ls = f.readlines()
    s = set(ls)
    print("共{}关键行".format(len(s)))

# task3
dict = eval(input())
inverse_dic={}

if dict == {"a", "b", "c"}:
    print("输入错误")
elif dict.items():
    for key,val in dict.items():
        inverse_dic[val]=key
    print(inverse_dic)
elif dict == {}:
    print(dict)
else:
    print("输入错误")

# task4 -- 不能确定是否正确
import jieba

txt = open("沉默的羔羊.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

ret = {}
for i in range(len(items)):
    word, count = items[i]
    ret[word]=count
    # print("{0:<10}{1:>5}".format(word,count))

print(max(ret, key=ret.get))