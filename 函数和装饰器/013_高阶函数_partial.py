# -*- coding:utf-8 -*-
from functools import partial

print("1 ---------------------------------------------")

"""
int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换，其中有一个 base 参数可以指定转换的进制。
"""

print(int('123'))
print(int('123', base=8))
print(int('a', base=16))
print(int('101', base=2))

print("2 ---------------------------------------------")

"""
如果要转换大量的十六进制字符串，每次都传入 base = 16 就很繁琐，
为了简便可以想到定义一个 hexstr2int() 的函数，默认把 base = 16 传进去：
"""


def hexstr2int(x):
    return int(x, base=16)


print(hexstr2int('a'))

print("3 ---------------------------------------------")
# functools.partial() 方法可以直接创建一个这样的函数，而不需要自己定义 hexstr2int():
hexstr2int_c = partial(int, base=16)
print(hexstr2int_c('a'))
print(type(hexstr2int_c))  # <class 'functools.partial'>


# 注意到它返回的是一个 functools.partial 类型，而不是一个普通的函数，hexstr2int_c等价于定义了一个如下的函数：
def hexstr2int_c_(x):
    args = (x)
    kwargs = {'base': 16}

    return int(*args, **kwargs)


print("4 ---------------------------------------------")
# 如果我们不使用关键字参数，而是直接使用值，那么将作为位置参数传递给 int()，例如：
hexstr2int_d = partial(int, 'a')


# hexstr2int_d 等价于
def hexstr2int_d_(x):
    args = ('a')
    kwargs = {'base': x}

    return int(*args, **kwargs)


print(hexstr2int_d(16))

print("5 ---------------------------------------------")


# 如果一个函数有多个参数，那么就要区分这种参数的传递关系，我们看一个示例：
def func(a, b, c, d):
    print("a %d, b:%d c:%d, d:%d" % (a, b, c, d))
    return a * 4 + b * 3 + c * 2 + d


part_func1 = partial(func, 1, d=4)
part_func1(2, 3)

part_func2 = partial(func, b=1, d=4)
part_func2(2, c=3)

part_func0 = partial(part_func2, c=3)  # 嵌套
part_func0(2)

"""
使用 partial() 的目的是为简化代码，让代码简洁清晰，但也要注意到它的副作用，
由于它返回 functools.partial 类型，隐藏了某些逻辑，比如新函数没有函数名，让跟踪更困难。
"""
