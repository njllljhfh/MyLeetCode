# -*- coding:utf-8 -*-
def action(methods):
    def deco(view):
        view.allow_methods = [method.lower() for method in methods]
        return view

    return deco


@action(['GET', 'POST'])
def view(request):
    if request.method.lower() in view.allow_methods:
        print(111)


class R(object):
    def __init__(self):
        self.method = 'POST'


if __name__ == '__main__':
    r = R()
    print(r.method)
    # view(r)
    print(view.__dict__)
