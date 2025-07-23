# -*- coding:utf-8 -*-
import sys


def solution():
    a, b = 1, 2

    def fibonacci():
        nonlocal a, b
        a, b = b, a + b
        return a

    return fibonacci


if __name__ == '__main__':
    so = solution()

    print(so())
    print(so())
    print(so())
    print(so())
    print(so())
    print("- " * 30)

