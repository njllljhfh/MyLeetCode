# -*- coding:utf-8 -*-


def factorial1():
    """阶乘：闭包实现"""
    a = 0
    b = 1

    def inner():
        nonlocal a, b
        if a == 0:
            a = 1
            b = 1
        res = a
        a, b = a * b, b + 1
        return res

    return inner


def factorial2():
    """阶乘：生成器实现"""
    a = 0
    b = 1
    while True:
        if a == 0:
            a = 1
            b = 1
        res = a
        a, b = a * b, b + 1
        yield res


if __name__ == '__main__':
    print("阶乘：闭包实现")
    factorial_1 = factorial1()

    for i in range(6):
        print(factorial_1())

    print("----------------------------------------------")

    print("阶乘：生成器实现")
    factorial_2 = factorial2()

    for i in range(6):
        print(next(factorial_2))
