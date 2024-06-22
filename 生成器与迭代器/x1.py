# -*- coding:utf-8 -*-


# def solution():
#     a = 1
#     b = 1
#
#     def f():
#         nonlocal a, b
#         yield a
#         while True:
#             a, b = b, a + b
#             yield a
#
#     return f()
#
#
# if __name__ == '__main__':
#     myx = solution()
#     print(next(myx))
#     print(next(myx))
#     print(next(myx))
#     print(next(myx))
#     print(next(myx))
#     print(next(myx))


def solution():
    a, b = 1, 2

    def next_fibonacci():
        nonlocal a, b
        a, b = b, a + b
        return a

    return next_fibonacci


if __name__ == '__main__':
    myx = solution()

    print(myx())
    print(myx())
    print(myx())
    print(myx())
    print(myx())

    print(myx.__code__.co_freevars)
    print(myx.__closure__[0].cell_contents, myx.__closure__[1].cell_contents)
    print("-" * 30)

    print(myx())  # 输出第二个斐波那契数
    print(myx.__code__.co_freevars)
    print(myx.__closure__[0].cell_contents, myx.__closure__[1].cell_contents)
    print("-" * 30)

    print(myx())  # 输出第三个斐波那契数
    print(myx.__code__.co_freevars)
    print(myx.__closure__[0].cell_contents, myx.__closure__[1].cell_contents)
    print("-" * 30)

    print(myx())  # 输出第四个斐波那契数
    print(myx.__code__.co_freevars)
    print(myx.__closure__[0].cell_contents, myx.__closure__[1].cell_contents)
    print("-" * 30)

    print(myx())  # 输出第五个斐波那契数
    print(myx.__code__.co_freevars)
    print(myx.__closure__[0].cell_contents, myx.__closure__[1].cell_contents)
    print("-" * 30)


    def xxx():
        for i in range(10):
            yield i

    x = xxx()
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())

# def foo():
#     a = 'free var'
#
#     def bar():
#         nonlocal a
#         print(a)
#         a = "666"
#
#     return bar
#
#
# bar = foo()
# bar()
# print(bar.__code__.co_freevars)
# print(bar.__closure__)
# print(bar.__closure__[0].cell_contents)


def decorate(func):
    print('running decorator when import')
    return func


@decorate
def foo():
    print('running foo')
    pass


# if __name__ == '__main__':
#     print('start foo')
#     foo()
