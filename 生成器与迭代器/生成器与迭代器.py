# -*- coding:utf-8 -*-
import sys
import types
from typing import Iterator

list0 = [x * x for x in range(5)]
print(list0)

list_generator0 = (x * x for x in range(5))
print(list_generator0)
for i in list_generator0:
    print(f"i = {i}")
print("- " * 30)

list_generator1 = (x * x for x in range(5000000))
print(sys.getsizeof(list_generator0))
print(sys.getsizeof(list_generator1))
print("- " * 30)

list_generator0 = (x * x for x in range(3))
print(next(list_generator0))
print(next(list_generator0))
print(next(list_generator0))
# print(next(list_generator0))  # 触发 StopIteration 异常
print("- " * 30)


def fib_generator(n):
    i, j = 0, 1

    while (i < n):
        yield i
        i, j = j, i + j


print(isinstance(fib_generator(5), types.GeneratorType))
print(isinstance(fib_generator(5), Iterator))
print(type(fib_generator))
print(type(fib_generator(5)))
f = fib_generator(5)
print(next(f))
print(next(f))
print(next(f))
print("------------------------------------------------------")

list_generator0 = (x * x for x in range(3))
print('__iter__' in dir(list_generator0))
print('__next__' in dir(list_generator0))
print(dir(list_generator0))
print("------------------------------------------------------")
fg = fib_generator(5)
print('__iter__' in dir(fg))
print('__next__' in dir(fg))
print(dir(fg))
print("------------------------------------------------------")


# 判断可迭代对象
def is_iterable(obj):
    status = True
    try:
        iter(obj)
    except TypeError:
        status = False
    return status


# 判断迭代器对象
def is_iterator(obj):
    return is_iterable(obj) and obj is iter(obj)

print(is_iterable(fg))
print(is_iterator(fg))