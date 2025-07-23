# -*- coding:utf-8 -*-
"""
如果我们需要对一个函数既要统计运行时间，又要记录运行日志，如何使用装饰器呢？
Python 函数或类也可以被多个装饰器修饰，也即装饰器嵌套（Decorator Nesting）。
要是有多个装饰器时，这些装饰器的执行顺序是怎么样的呢？


可以看到按照 markbold(markitalic(markstr())) 的顺序执行，
多个装饰器按照靠近被修饰函数或者类的距离，由近及远依次执行的（这里的执行，指的是执行装饰器最内部，包含f()调用的代码）。
"""
from functools import wraps

"""
装饰器是导入的时候就加载，即在内层闭包函数被调用前。
"""


def markbold(f):
    print("markbold--------------start")  # 函数调用前 --- 3

    # @wraps(f)
    def y():
        print("y________start")  # 函数调用后，step 1
        b = '<b>' + f() + '</b>'  # 函数调用后，step 2，执行 f() 相当于执行 markitalic 中的 x(), 并将执行结果与b标签进行字符串连接，然后赋值给变量 b
        print("y________end")  # 函数调用后，step 8
        return b  # 函数调用后，step 9

    print("markbold--------------end")  # 函数调用前 --- 4

    return y


def markitalic(f):
    print("markitalic--------------start")  # 函数调用前 --- 1

    # @wraps(f)
    def x():
        print("x________start")  # 函数调用后，step 3
        a = '<i>' + f() + '</i>'  # 函数调用后，step 4 (整行代码都执行了)
        print("x________end")  # 函数调用后，step 6
        return a  # 函数调用后，step 7

    print("markitalic--------------end")  # 函数调用前 --- 2
    return x


@markbold
@markitalic  # 函数真正调用前，先装饰的装饰器(距离函数近的)，先加载
def markstr():
    return "Python"  # 函数调用后，step 5


print("------------------ 函数调用前 ------------------")
print(markstr())

print("------------------ 查看被装饰函数的信息 ------------------")
"""
装饰器极大地复用了代码，但是一个缺点就是原函数的元信息不见了，比如函数的 docstring，__name__，参数列表。 
这是一个严重的问题，当进行函数跟踪，调试时，或者根据函数名进行判断的代码就不能正确执行，这些信息非常重要。


functools 模块中的 wraps 可以帮助保留这些信息。functools.wraps 本身也是一个装饰器，它把被修饰的函数元信息复制到装饰器函数中，这就保留了原函数的信息。
其实 functools.wraps 并没有彻底恢复所有函数信息，具体请参考第三方模块 wrapt。
"""

# 不加 @wraps ----- y
# 加 @wraps ----- markstr
print(markstr.__name__)
