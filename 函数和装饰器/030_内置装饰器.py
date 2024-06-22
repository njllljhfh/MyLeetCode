# -*- coding:utf-8 -*-
"""
定义类静态方法
    @staticmethod 装饰器将类中的方法装饰为静态方法，不需要创建类的实例，可以通过类名直接引用。实现函数功能与实例解绑。
    静态方法不会隐式传入参数，不需要传入 self ，类似一个普通函数，只是可以通过类名或者类对象来调用。
"""


class C(object):
    @staticmethod
    def static_method():
        print("This is a static method!")


C.static_method()  # 类名直接调用

c = C()
c.static_method()  # 类对象调用

print("---------------------------------------------------")

"""
定义类方法
    @classmethod 装饰器用于定义类方法，类方法和类的静态方法非常相似，只是会隐式传入一个类参数 。类方法被哪个类调用，就传入哪个类作为第一个参数进行操作。
"""


class C2(object):
    @classmethod
    def class_method(cls):
        print("This is ", cls)


class B2(C2):
    pass


C2.class_method()  # 类名直接调用
c2 = C2()
c2.class_method()  # 类对象调用

B2.class_method()  # 继承类调用
print("---------------------------------------------------")

"""
实例方法属性化
    property(fget=None, fset=None, fdel=None, doc=None) -> property attribute

内置方法 property() 可以将类中定义的实例方法（对象方法）属性化，可以直接为成员赋值和读取，也可以定义只读属性。
"""


class C3(object):

    def __init__(self):
        self.__arg = 0

    def getarg(self):
        return self.__arg

    def setarg(self, value):
        self.__arg = value

    def delarg(self):
        del self.__arg

    arg = property(fget=getarg, fset=setarg, fdel=delarg, doc="'arg' property.")


c3 = C3()
c3.arg = 10  # 调用 setarg
print(c3.arg)  # 调用 getarg

c3.setarg(20)  # 调用 setarg
print(c3.getarg())  # 调用 getarg
del c3.arg  # 调用 delarg
# print(c3.arg) # 删除后调用，报错 AttributeError: 'C3' object has no attribute '_C3__arg'
print("---------------------------------------------------")

"""
如果不提供 fset 参数，则属性就变成只读的了。@property 装饰器以更简单的方式实现了相同功能。

注意三个方法的命名必须相同，getter（在 prorperty() 中名为 fget）对应的方法总是用 “@property” 修饰，
其他两个为方法名加上 “.setter” 和 “.deleter”，如果定义只读属性，不定义 setter 方法即可。
"""


class C4(object):
    def __init__(self):
        self.__arg = 0

    @property
    def argopt(self):
        return self.__arg

    @argopt.setter
    def argopt(self, value):
        self.__arg = value

    @argopt.deleter
    def argopt(self):
        del self.__arg


c4 = C4()
c4.arg = 10
print(c4.arg)
del c4.arg
