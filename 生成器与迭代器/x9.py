# -*- coding:utf-8 -*-
# from one.x8 import foo8

# foo8


import types


def deco(cls):
    for key, method in cls.__dict__.items():
        if isinstance(method, types.FunctionType):
            print(key, ':', method.__name__)
    return cls


@deco
class Test:
    def __init__(self):
        pass

    def foo(self):
        pass


print(Test.__dict__)
