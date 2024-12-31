#!/usr/bin/env python
# coding:utf-8

# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000

'''
关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
'''


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# 限制的参数有几个就必须填几个
def person2(name, age, *, city, job):
    print(name, age, city, job)


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
# name, age  为位置参数
# 命名关键字参数可以有缺省值
def person3(name, age, *args, city='Zhejiang', job):
    print(name, age, args, city, job)

extra = {'city': 'Beijing', 'job': 'Engineer', 'gender': 'Male'}

if __name__ == '__main__':
    person("Tom", 32)
    person("Bob", 35, city='Beijing', gender="Male")
    person("Bob", 35, job="Engineer")
    print("----run person() with **kw----")
    person("Jack", 24, city=extra['city'], job=extra['job'])
    person("Jack", 24, **extra)
    print("------限制关键字参数的名字 run person2()-------")
    person2("Jack", 24, city='Shanghai', job='PM')
    print("------命名关键字参数的名字 run person3()-------")
    person3("Jack", 24, city='Beijing', job='Engineer')
    person3("Jack", 24, job='Engineer')
    person3("Jack", 24, "Company", city='Beijing', job='Engineer')



