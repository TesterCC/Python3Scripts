import re

# 实现一个函数，判断一个字符串是否为回文字符串（忽略大小写和非字母字符）

def is_palindrome(s):
    # use regex to filter out non-alphabetic characters and convert the string to lowercase
    s = re.sub(r'[^a-zA-Z]', '', s).lower()
    # check if the processed string is the same as itself reverse
    return s == s[::-1]


# test example
testcase1 = "A man, a plan, a canal: Panama"
print(is_palindrome(testcase1))

testcase2 = "He lived as 56 * a devil, eh?"
print(is_palindrome(testcase2))
