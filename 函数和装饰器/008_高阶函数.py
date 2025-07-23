# -*- coding:utf-8 -*-

"""
functools 模块提供了一系列的重量级函数，这些函数有一个特点，函数调用其他函数完成复杂功能，
或把一个函数作为返回值，这类函数被称为高阶（Higher-order）函数。
由于历史原因，多数高阶函数从内置函数中封装进 functools 模块，有些函数还没有，比如 map()。
"""

# print(f"测试元组中的可变类型元素是否能修改值")
# a = ([], [], [])
# print(a)
# print(id(a[0]))
#
# a[0].append(0)
# a[1].append(1)
# a[2].append(2)
# print(a)
# print(id(a[0]))
