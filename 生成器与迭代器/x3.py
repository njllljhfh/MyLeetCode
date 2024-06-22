# -*- coding:utf-8 -*-
view_registry = []


def register(func):
    view_registry.append(func)
    return func


@register
def view1():
    pass


@register
def view2():
    pass


def main():
    print(view_registry)


if __name__ == '__main__':
    main()
