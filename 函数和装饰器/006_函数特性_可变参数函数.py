# -*- coding:utf-8 -*-
def test_args(*args, **kwargs):
    print(args)
    print(kwargs)


# test_args() 是一个可以接受任意多个参数的函数。由于参数处理是有优先级的，kwargs 和 args 顺序不可颠倒。
test_args(1, 2, {"key0": "val0"}, name="name", age=18)

print("---------------------------------------------------------")


def x(a, *args, b=10, **kwargs):
    print(f"a = {a}")
    print(f"args = {args}")
    print(f"b = {b}")
    print(f"kwargs = {kwargs}")


x(1, 2, 3, 4, b=100, x=21, y=22, z=23)
