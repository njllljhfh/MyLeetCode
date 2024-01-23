# -*- coding:utf-8 -*-


def fib(num):
    x, y = 1, 1
    for _ in range(num):
        yield x
        x, y = y, x + y


if __name__ == '__main__':
    n = 10
    for i in fib(n):
        print(i)
