# -*- coding:utf-8 -*-
"""
以上介绍了函数作为装饰器去装饰其他的函数或者类方法，那么可不可以让一个类发挥装饰器的作用呢？
答案是肯定的。 而且，相比装饰器函数，装饰器类具有更大灵活性，高内聚，封装性特点。


装饰器类必须定义 __call__() 方法，它将一个类实例变成一个用于装饰器的方法(把类对象变成可调用对象)。
"""

print("-------------------- 无参装饰器类 --------------------")


class Tracer(object):
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("call %s() %d times" % (self.func.__name__, self.calls))
        return self.func(*args, **kwargs)


@Tracer
def test_tracer(val, name="default"):
    print("func() name:%s, val: %d" % (name, val))


for i in range(2):
    test_tracer(i, name=("name" + str(i)))

"""
上面的装饰器和for循环，相当于执行如下代码：

t = Tracer(test_tracer)
for i in range(2):
    t(i, name=("name" + str(i)))  # 会调用__call__方法
    
"""

print("-------------------- 带参数装饰器类 --------------------")

"""
装饰器类的参数需要通过类方法 __init__() 传递，所以被装饰的函数就只能在 __call__() 方法中传入，
为了把函数的参数传入，必须在 __call__() 方法中再封装一层。
"""


class Tracer2(object):
    def __init__(self, arg0):  # 可支持任意参数
        self.arg0 = arg0
        self.calls = 0

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            self.calls += 1
            print("arg0:%d call %s() %d times" % (self.arg0, func.__name__, self.calls))
            return func(*args, **kwargs)

        return wrapper


@Tracer2(arg0=0)
def test_tracer2(val, name="default"):
    print("func() name:%s, val: %d" % (name, val))


for i in range(2):
    test_tracer2(i, name=("name" + str(i)))

"""
上面的装饰器和for循环，相当于执行如下代码：

t2 = Tracer2(arg0=0)
t2 = t2(test_tracer2)
for i in range(2):
    t2(i, name=("name" + str(i)))
    
"""
