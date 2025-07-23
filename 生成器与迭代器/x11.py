# -*- coding:utf-8 -*-
def decorate(func):
    print('running decorator when import')
    b = 666

    def wrapper(a, *args, **kwargs):
        if a == 10:
            return b
        else:
            return func(a, *args, **kwargs)

    return wrapper


@decorate
def mytest(a):
    print(f"a = {a}")
    return a


if __name__ == '__main__':
    x = 10
    print(mytest.__code__.co_freevars)
    print(mytest.__closure__)
    print(mytest(x))
