# -*- coding:utf-8 -*-
def test_input_args(list0, num0, name="Tom"):
    print("list:%s, num:%d, name:%s" % (str(list0), num0, name))


test_input_args([1], 2, name="John")
test_input_args(*([1], 2), **{"name": "John"})

print("--------------------------------------------------------------")


def func0(n):
    print("from %s, %d" % (func0.__name__, n))


def func1(m, n):
    print("from %s, %d" % (func0.__name__, m + n))


def test_call_func(func, *args, **kwargs):
    func(*args, **kwargs)


test_call_func(func0, 1)
test_call_func(func1, 1, 2)
