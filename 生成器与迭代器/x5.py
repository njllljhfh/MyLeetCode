# -*- coding:utf-8 -*-
def deco_factory(*args, **kwargs):
    def deco(func):
        print(args)
        return func

    return deco


@deco_factory('factory')
def foo5():
    pass


foo5()
