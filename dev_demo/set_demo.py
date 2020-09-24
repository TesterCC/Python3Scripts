# coding=utf-8
'''
DATE: 2020/09/24
AUTHOR: Yanxi Li
'''

# set(a)-set(b)   # 计算前者有，后者没有的元素

a = ["x", "y", "z"]

b = ["x", "z"]

c = ["a", "b", "x"]

print(f"set a is : {set(a)}")
print(f"set b is : {set(b)}")

# set(a) 中有，但 set(b) 没有
print(f"set a-b is : {set(a) - set(b)}")

# set(b) 中有，但 set(a) 中没有
print(f"set b-a is : {set(b) - set(a)}")

# set(c) 中有，但 set(a) 中没有
print(f"set c-a is : {set(c) - set(a)}")
