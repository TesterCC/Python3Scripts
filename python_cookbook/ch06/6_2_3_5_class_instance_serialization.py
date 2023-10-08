# -*- coding=utf-8 -*-
import json

# P184-185
'''
类实例一般是无法序列化为JSON的
如果想序列化类实例，可提供一个函数将类实例作为输入并返回一个可以被序列化处理的字典
P.S.: 元编程一般场景用不上，但还是应该了解学习
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    # print(">>>", vars(obj))  # debug
    d.update(vars(obj))
    # print(">>>", d)          # debug
    return d


# get a instance

# Dictionary mapping names to known classes
classes = {
    'Point': Point
}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)  # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d


if __name__ == '__main__':
    # example
    p = Point(2, 3)
    s = json.dumps(p, default=serialize_instance)
    print(type(s), " --- ", s)

    a = json.loads(s, object_hook=unserialize_object)
    print(type(a), " --- ", a)

    print(a.x)
    # print(a.y)  # fixme: report err
