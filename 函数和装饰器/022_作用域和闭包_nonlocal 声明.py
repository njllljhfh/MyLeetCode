# -*- coding:utf-8 -*-
"""
与 global 声明类似，nonlocal 声明可以在闭包中声明使用上一级作用域中的变量。
"""


def foo():
    a = 0

    def bar():
        nonlocal a
        a += 1
        return a

    return bar


c = foo()
print(c())
print(c())

"""
使用 nonlocal 声明 a 为上一级作用域中的变量 a，就解决了该问题，可以实现累加了。
注意 nonlocal 关键字只能用于内嵌函数中，并且外层函数中定义了相应的局部变量，否则报错。
"""
# 下面代码报错
# var = 100
# def t():
#     nonlocal var
#     var += 1
#     print(var)
# print(t())
