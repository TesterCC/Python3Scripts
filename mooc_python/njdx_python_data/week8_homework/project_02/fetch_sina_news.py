#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-06 21:58'

'''
项目2：动态新闻标题热点挖掘
以获取一定时间段内新闻标题中的热点词并绘制词云

1.从新闻网站爬取若干新闻标题并进行解析
2.标题分词(Text Segmentation)
3.去除停用词
4.选择名词
5.根据词频画出词云
'''

import jieba.posseg as pseg
import matplotlib.pyplot as plt
from os import path
import re
import requests
from scipy.misc import imread
# import imageio
from wordcloud import WordCloud


def fetch_sina_news():
    # set basic info
    PATTERN = re.compile('"title":(.*?),')
    BASE_URL = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&nu%20m=50&page=1&r=0.07257693576113322'

    # MAX_PAGE_NUM = 10
    with open('subjects.txt', 'w', encoding='utf-8') as f:
        r = requests.get(BASE_URL)

        # unicode to utf-8 code, python3
        data = r.text.encode('utf-8').decode('unicode-escape')
        p = re.findall(PATTERN, data)
        for s in p:
            f.write(s)


def extract_words():
    with open('subjects.txt', 'r', encoding='utf-8') as f:
        new_subjects = f.readlines()  # txt file must not too large

    stop_words = set(line.strip() for line in open('stopwords.txt', encoding='utf-8'))

    newslist = []

    for subject in new_subjects:
        # when obj is space, stop current loop, jump to next loop
        if subject.isspace():
            continue

        # segment word line by line
        # n,nr,ns ... art the flags of nouns
        p = re.compile("n[a-z0-9]{0,2}")
        word_list = pseg.cut(subject)
        for word, flag in word_list:
            if not word in stop_words and p.search(flag) != None:
                newslist.append(word)

    # 手动计算词频
    content = {}

    for item in newslist:
        content[item] = content.get(item, 0) + 1

    d = path.dirname(__file__)
    print(d)
    print(content)

    # FIXME cannot find path on Mac OS
    mask_image = imread(path.join(d, "mickey.png"))  # removed in scipy 1.2.0, use imageio.imread
    # mask_image = imageio.imread(path.join(d, "mickey.png"))
    # 利用 WordCloud()函数基于词创建词云，这里选择词频最高的 10 个词
    wordcloud = WordCloud(font_path='simhei.ttf', background_color="grey", mask=mask_image,
                          max_words=10).generate_from_frequencies(content)

    # Display the generated image
    plt.imshow(wordcloud)
    plt.axis("off")
    wordcloud.to_file('wordcloud.jpg')
    plt.show()


if __name__ == '__main__':
    fetch_sina_news()
    extract_words()
