# coding=utf-8
"""
DATE:   2020/11/23
AUTHOR: Yanxi Li
DESCRIPTION:
https://zhuanlan.zhihu.com/p/34671514

利用nltk删除英文停用词

由于一些常用字或者词使用的频率相当的高，英语中比如a，the, he等，中文中比如：我、它、个等，每个页面几乎都包含了这些词汇，
如果搜索引擎它们当关键字进行索引，那么所有的网站都会被索引，而且没有区分度，所以一般把这些词直接去掉，不可当做关键词。

Noted：
nltk自带stopwords效果不好，一般需要自己准备。
通用的根据语料库corpus收集，找有专业方向基础停用词库的人要。
不同研究方向一般有不同的停用词，可能要自己一次次跑，一点点归纳。
"""

from nltk.corpus import stopwords

stop_words = stopwords.words('english')
print(len(stop_words))

# extend stopwords from yourself
ext_stopwords = ['!', ',' ,'.' ,'?' ,'-s' ,'-ly' ,'</s> ', 's']

for word in ext_stopwords:
    stop_words.append(word)

print(len(stop_words))
print(stop_words)

# 假设语料在word_list中
word_string = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna, aliqua. 
It's just a testing. From here you can search these documents. 
Enter your search words into the box below and click "search". 
Note that the search function will automatically search for all of the words. 
Pages containing fewer words won't appear in the result list.
'''
word_list = word_string.split()

print(len(word_list))

filtered_words = [word for word in word_list if word not in stopwords.words('english')]

print(len(filtered_words))