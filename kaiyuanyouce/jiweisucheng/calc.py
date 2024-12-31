# -*- coding:utf-8 -*-


class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # 重置数据
    def set(self, a, b):
        self.a = a
        self.b = b

    # 加法
    def add(self):
        return self.a + self.b

    # 减法
    def sub(self):
        return self.a - self.b

    # 乘法
    def mul(self):
        return self.a * self.b

    # 除法
    def div(self):
        if b != 0:
            # 保留小数点后4位
            return round(self.a / self.b, 4)

        raise ("除数为0，非法")


def test(calc):

    sum = calc.add()

    sub = calc.sub()

    mul = calc.mul()

    div = calc.div()

    print(sum, sub, mul, div)


if __name__ == "__main__":

    a = int(input("请输入第1个数据："))
    b = int(input("请输入第2个数据："))
    
    # 测试各函数
    calc = Calc(a, b)
    test(calc)

    # 重置一下
    calc.set(5, 6)
    test(calc)
