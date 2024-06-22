# -*- coding:utf-8 -*-
"""
尽管闭包函数可以引用外层函数中的变量，但是这个变量不能被动态改变。

在 函数作为返回值 一节中（017_作用域和闭包_函数作为返回值.py），
已经看到 Python 在把函数作为返回值时，并不会把函数体中的全局变量替换为实际的值，而是原封不动的保留该变量。
那么当这种情况出现在闭包中会怎样呢？
"""


def fun():
    flist = []
    for i in range(3):
        def foo(x):
            print(x + i, end=' ')

        flist.append(foo)
    return flist


flist = fun()
for f in flist:
    f(1)

print("\n----------------------------------------------------------")
"""
结果是一样的，如果一个变量已被闭包函数引用，那么就要保证这个变量不会再被改变，否则闭包函数的行为将难以预知。
除了 for 循环以外，while 循环也会导致相同问题。
"""


# 改进方法
def fun():
    flist = []
    for i in range(3):
        def foo(x, y=i):  # 将i变为 foo 函数参数，参数 y 也属于 foo 函数的局部变量
            print(x + y, end=' ')

        flist.append(foo)
    return flist


flist = fun()
for f in flist:
    f(1)
