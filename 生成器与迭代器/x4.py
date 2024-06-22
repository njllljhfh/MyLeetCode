# -*- coding:utf-8 -*-
import copy

from x5 import foo5


def fresh_defaults(func):
    defaults = func.__defaults__

    def deco(*args, **kwargs):
        func.__defaults__ = copy.deepcopy(defaults)
        return func(*args, **kwargs)

    return deco


@fresh_defaults
def foo(x, y=[]):
    y.append(x)
    print(y)


foo(1)
foo(2)
foo(3)
# foo5()
