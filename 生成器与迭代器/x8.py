# -*- coding:utf-8 -*-

def d1(func):
    print("d1")

    def wrapper():
        print("d1----------")
        return func()

    return wrapper


def d2(func):
    print("d2")

    def wrapper():
        print("d2----------")
        return func()

    return wrapper


@d1
@d2
def foo8():
    print("foo8")
    pass


foo8()
