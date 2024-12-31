# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/14 17:06'


class DemoClass:
    """
    定义一个基本类
    """
    def __int__(self):
        print("初始化")

    def output(self, text):
        # 输出text到console
        print(text)

    def output_none(self):
        # 不带参数的方法
        print("我不能传入参数")


class ChildDemoClass(DemoClass):
    """
    对基础示例扩展 继承DemoClass
    """

    def __init__(self):
        print("我是子类")

    def output_none(self):
        """
        重写output_none
        """
        print("我是子类不能传参的方法")


if __name__ == '__main__':
    # 创建一个类对象
    demo_obj = DemoClass()

    # 调用output
    demo_obj.output("我是传入的参数1")

    # 调用output_none
    demo_obj.output_none()

    print("-"*50)

    # 创建子类的对象
    child_demo_obj = ChildDemoClass()

    # 调用output, 调用的是父类的方法
    child_demo_obj.output("我是传入参数2")

    # 调用output_none, 调用的是自己的方法，即重写后的方法
    child_demo_obj.output_none()

