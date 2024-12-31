# coding=utf-8
"""
DATE:   2020/12/9
AUTHOR: Yanxi Li
DESC: 阅读数据集并建立垃圾邮件黑名单
"""

import os
"""
Download 2007 TREC Public Spam Corpus
Read the "Agreement for use" https://plg.uwaterloo.ca/~gvcormac/treccorpus07/

Download 255 MB Corpus (trec07p.tgz) and untar into the 'chapter1/datasets' directory

Check that the below paths for 'DATA_DIR' and 'LABELS_FILE' exist
"""

DATA_DIR = 'datasets/trec07p/data/'
LABELS_FILE = 'datasets/trec07p/full/index'
TRAINING_SET_RATIO = 0.7

labels = {}
spam_words = set()
ham_words = set()

# Read the labels
# todo P16-17 , jupyter notebook E:\github_open\mlsec\book-resources\       chapter1/spam-fighting-blacklist.ipynb
