# -*- coding:utf-8 -*-
"""
所谓类装饰器，就是对类进行装饰的函数或者类。
从装饰器的本质，我们知道，一个对函数进行装饰的装饰器函数，
它的语法糖被解释的时候，默认转换为如下形式：

@decorator
def func():
    ......

func = decorator(func)
func()

"""

"""
如果使用装饰器类，则进行如下转换：

class decorator():
    .....

@decorator
def func():
    ......

instance = decorator(func)
func = instance.__call_()
func()

"""

"""
所以装饰一个函数，就是对函数进行封装，就要把被装饰的函数传递给装饰器，如果要装饰一个类，那么就要把类传递给装饰器。
"""

print("-------------------- 使用函数装饰类 --------------------")

"""
DotClass 类原本是一个空类，既没有成员变量也没有方法，
我们使用函数动态的为它添加类成员 x 和 y，以及类方法 move()，
唯一要注意的是 move() 方法第一个参数一定是 self，在类对象调用它时，它对应实例自身。
"""


class DotClass(object):
    pass


def class_add_method(Class):
    Class.x, Class.y = 0, 0

    def move(self, a, b):
        self.x += a
        self.y += b
        print("Dot moves to (%d, %d)" % (self.x, self.y))

    Class.move = move
    return Class


DotClass = class_add_method(DotClass)
dot = DotClass()
dot.move(1, 2)


# 可以看到上面的行为很像装饰器的过程，我们使用语法糖 @ 来测试下，是否如预期一样：
@class_add_method
class DotClass2(object):
    pass


dot2 = DotClass2()
dot2.move(3, 4)

print("-------------------- 使用函数装饰类（返回新类） --------------------")


# 以上示例我们只是为类安装了参数和方法，返回原来的类，我们也可以定义一个新类，并返回它。
def class_add_method_new(Class):  # @语句处调用
    class Wrapper(object):
        def __init__(self, *args):  # 创建实例时调用
            self.wrapped = Class(*args)  # 调用 DotClass3.__init__

        def move(self, a, b):
            self.wrapped.x += a
            self.wrapped.y += b
            print("Dot moves to (%d, %d)" % (self.wrapped.x, self.wrapped.y))

        def __getattr__(self, name):  # 对象获取属性时调用
            return getattr(self.wrapped, name)

    return Wrapper


@class_add_method_new
class DotClass3(object):  # DotClass3 = class_add_method_new(DotClass3)
    def __init__(self):  # 在 Wrapper.__init__ 中调用
        self.x, self.y = 0, 0


dot3 = DotClass3()  # dot3 = Wrapper()
dot3.move(5, 6)
print(dot3.x)  # 调用 Wrapper.__getattr__

"""
上边的装饰器写法，相当于不加装饰器，执行下面的代码
DotClass3 = class_add_method_new(DotClass3)
dot3 = DotClass3()
dot3.move(5, 6)
print(dot3.x)
"""

"""
示例中，我们返回了一个新的类，要注意的是，新的初始化函数封装了对原来类的实例化调用，并在新增的方法中引用原来类中成员，
此外由于新类并不感知被装饰类的成员，所以必须实现 __getattr__() 方法。
"""

print("-------------------- 使用带参函数装饰类 --------------------")


def decorator(arg0=0):
    def class_add_method_new(Class):
        class Wrapper(object):
            def __init__(self, *args, **kwargs):
                self.wrapped = Class(*args, **kwargs)

            def move(self, x, y):
                self.wrapped.x = x
                self.wrapped.y = y
                print(f"Dot moves to ({self.wrapped.x}, {self.wrapped.y}). arg0={arg0}")

            def __getattr__(self, item):
                return getattr(self.wrapped, item)

        return Wrapper

    return class_add_method_new


# @decorator(arg0=2)
class DotClass4(object):
    def __init__(self):  # 在 Wrapper.__init__ 中调用
        self.x, self.y = 0, 0


# dot4 = DotClass4()
# dot4.move(7, 8)
# print(dot4.x)

"""
@语句等价于:
decorator = decorator(arg0=2)
DotClass4 = decorator(DotClass4)
------------
dot4 = DotClass4()
dot4.move(7, 8)
print(dot4.x)
"""
