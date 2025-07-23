# -*- coding:utf-8 -*-
import inspect
import types
from types import GeneratorType
from typing import Iterable, Iterator


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


class FibGenerator(object):
    def __init__(self, n):
        self.__n = n

        self.__s0 = 0
        self.__s1 = 1
        self.__count = 0

    def __next__(self):  # 用于内建函数 next()
        if self.__count < self.__n:
            ret = self.__s0
            self.__s0, self.__s1 = self.__s1, (self.__s0 + self.__s1)
            self.__count += 1

            return ret
        else:
            raise StopIteration

    def __iter__(self):  # 用于 for 循环语句。实现了这个方法，就是可迭代的。
        return self


fg = FibGenerator(5)
print(type(fg))
print(f"fg 是迭代器吗？ --- ", isinstance(fg, Iterator))
print(f"fg 是可迭代的吗？ --- ", isinstance(fg, Iterable))
print(f"fg 是生成器吗？ --- ", isinstance(fg, types.GeneratorType))

for i in fg:
    print(i, end=' ')
print("\n--------------------------------------")

# list1 = (1, 2, 3)
list1 = {1: 1, 2: 2}
print(f"list1 是迭代器吗？ --- ", isinstance(list1, Iterator))
print(f"list1 是可迭代的吗？ --- ", isinstance(list1, Iterable))
print(f"list1 是生成器吗？ --- ", isinstance(list1, types.GeneratorType))
# print(next(list1)) # 列表无法用next调用，列表不是迭代器，列表式可迭代对象
print("\n--------------------------------------")

print(is_iterable(fg))
print(is_iterator(fg))

print("\n--------------------------------------")
# 只处理 2 和 3
list0 = [1, 2, 3]
for i in iter(list0.pop, list0[0]):
    print(i)
