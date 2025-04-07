# https://www.bilibili.com/video/BV1Lk4y117Cb?p=6

s0 = "1234567"
s1 = "  abc123  "
s2 = "ABCdefGHij"


print(max(s2))  # j
print(min(s2))  # A
print("-"*33)
print(s0.isdigit())
print(s1.isdigit())
print("-"*33)
print(s0.isalpha())
print(s1.isalpha())
print("-"*33)
print(s1.lstrip())  # delete left space
print(s1.rstrip())  # delete right space
print("-"*33)
print(s1.swapcase())   # ABC123  大小写字母反转
print(s2.swapcase())   # abcDEFghIJ