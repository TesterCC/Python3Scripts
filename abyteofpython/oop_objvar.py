#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-02-26 15:04'

"""
version 4.0  P102

Field   字段 有2种类型：
Class Variable    类变量   (Shared)
Object Variable   对象变量

# P104 当一个Object Variable和一个Class Variable名称相同时，Class Variable将会被隐藏

Robot.population，还可以使用self.__class__.population来使用，因为每个对象都通过self.__class__属性来引用它的Class
"""


class Robot:
    """a robot with name
    """
    population = 0    # belongs to Class Robot, Class Variable

    def __init__(self, name):
        """
        initial data
        """
        self.name = name   # Object Variable，Attribute Reference
        print("(Initializing {})".format(self.name))

        # 当有机器人被创建时，增加机器人数量
        Robot.population += 1

    def die(self):
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """A greeting from robot"""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """
        print current robots count
        """
        print("We have {:d} robots.".format(cls.population))


# Test
droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work at here.")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()


print("---Doc---")
print(Robot.__doc__)
print(Robot.say_hi.__doc__)