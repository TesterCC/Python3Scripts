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

# Extract subject and body text from a single email file
def extract_email_text(path):
    # Load a single email from an input file
    with open(path, errors='ignore') as f:
        msg = email.message_from_file(f)

    if not msg:
        return ""

    # Read the email subject
    subject = msg['Subject']
    if not subject:
        return ""

    # Read the email body
    body = ' '.join(m for m in flatten_to_string(msg.get_payload()) if type(m) == str)

    if not body:
        body = ""

    return subject + ' ' + body

# Process a single email file into stemmed tokens 将单个邮件处理成提取了词干的令牌符号
def load(path):
    email_text = extract_email_text(path)
    if not email_text:
        return []

    # Tokenize the message 令牌符号化消息
    tokens = nltk.word_tokenize(email_text)

    # Remove punctuation from tokens 删除tokens中的标点
    tokens = [i.strip("".join(punctuations)) for i in tokens if i not in punctuations]

    # Remove stopwords and stem tokens 删除停用词和词干化的tokens
    if len(tokens) > 2:
        return [stemmer.stem(w) for w in tokens if w not in stopwords]
    return []

