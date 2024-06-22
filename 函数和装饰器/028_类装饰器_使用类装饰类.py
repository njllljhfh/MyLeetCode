# -*- coding:utf-8 -*-
"""
注意使用装饰器的前提是为了更简便的实现功能，而不要为用而用，
装饰器和被装饰的函数或类应该是各自功能内聚，没有耦合关系。否则应该考虑其他方式，比如类继承。
在选择装饰器时，也应遵循先易后繁的原则，在装饰器函数不能满足需求时，才使用装饰器类。
"""

print("-------------------- 无参类装饰器 --------------------")


class Tracer(object):
    def __init__(self, Class):  # @语句处调用
        self.Class = Class

    def __call__(self, *args, **kwargs):  # 创建实例时调用
        self.wrapped = self.Class(*args, **kwargs)
        return self

    def move(self, x, y):
        self.wrapped.x = x
        self.wrapped.y = y
        print(f"{self.Class.__name__} moves to ({self.wrapped.x}, {self.wrapped.y})")

    def __getattr__(self, name):  # 获取属性时调用
        return getattr(self.wrapped, name)


@Tracer
class C(object):
    def __init__(self):
        self.x = 0
        self.y = 0


c = C()
c.move(1, 2)
print(c.x)

print("-------------------- 无参类装饰器 --------------------")


class TracerP(object):
    def __init__(self, arg0):  # @语句处调用
        self.arg0 = arg0

    def __call__(self, Class):
        self.Class = Class

        def wrapper(*args, **kwargs):  # 创建实例时调用
            self.wrapped = self.Class(*args, **kwargs)
            return self

        return wrapper

    def move(self, x, y):
        self.wrapped.x = x
        self.wrapped.y = y
        print(f"{self.Class.__name__} moves to ({self.wrapped.x}, {self.wrapped.y}). arg0={self.arg0}")

    def __getattr__(self, name):  # 获取属性时调用
        return getattr(self.wrapped, name)


@TracerP(arg0=1)
class D(object):
    def __init__(self):
        self.x = 0
        self.y = 0


d = D()
d.move(3, 4)
print(d.x)

"""
t = TracerP(arg0=1)
D = t(D)
d = D()
d.move(3, 4)
print(d.x)
"""
