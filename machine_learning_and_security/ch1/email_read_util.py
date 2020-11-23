# coding=utf-8
"""
DATE:   2020/11/19
AUTHOR: Yanxi Li
Machine Learning and Security P15-16

import nltk
nltk.download()
"""

import string
import email
import nltk

# 标点符号
punctuations = list(string.punctuation)
stopwords = set(nltk.corpus.stopwords.words('english'))    # use default english stopwords

# print(stopwords)
stemmer = nltk.PorterStemmer()

# Combine the different parts of the email info a flat list of strings
def flatten_to_string(parts):
    ret = []
    if type(parts) == str:
        ret.append(parts)
    elif type(parts) == list:
        for part in parts:
            ret += flatten_to_string(part)   # recursion
    elif parts.get_content_type == 'text/plain':
        ret += parts.get_payload()
    return ret

# todo


