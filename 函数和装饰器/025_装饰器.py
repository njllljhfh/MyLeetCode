# -*- coding:utf-8 -*-
"""
装饰器
从装饰的实现方式上可以分为装饰器函数和装饰器类，也即分别使用函数或者类对其他对象（通常是函数或者类）进行封装（装饰）。
"""
import logging.config
import time

from log_config.settings import LOGGING_DIC

logging.config.dictConfig(LOGGING_DIC)
logger = logging.getLogger(__name__)


def func(n):
    print("from func(), n is %d!" % (n), flush=True)


print("-------------------- 无参装饰器 --------------------")

"""
上面代码中的 wrapper() 是一个闭包，它接受一个函数作为参数，并返回一个新的闭包函数，
这个新的闭包函数对传入的函数进行了封装，也即起到了装饰的作用，所以包含了闭包的函数 log() 被称为装饰器。
运用装饰器可以在函数进入和退出时，执行特定的操作，比如插入日志，性能测试，缓存，权限校验等场景。
有了装饰器，就可以抽离出大量与函数功能无关的重复代码。
"""


def log(func):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        logger.debug('%s is called' % func.__name__)
        return ret

    return wrapper


func = log(func)
func(0)

"""
上面的写法还是不够简便，Python 为装饰器专门提供了语法糖 @ 符号。
无需在调用处修改函数调用方式，只需要在定义函数前一行加上装饰器。
"""


@log  # 添加装饰器 log()
def func2(n):
    print("from func2(), n is %d!" % (n), flush=True)


func2(0)

"""
以上语句相当于执行了如下操作：

func2 = log(func2)
func2(0)

"""

print("-------------------- 含参装饰器 --------------------")


def log3(level='debug'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            if level == 'warning':
                logger.warning("{} is called".format(func.__name__))
            else:
                logger.debug("{} is called".format(func.__name__))
            return ret

        return wrapper

    return decorator


# @log3()  # 由于装饰器 log3() 已经设置了默认参数，所以如果不需要传递参数给装饰器，那么直接使用 @log3() 即可（别忘了加括号）。
@log3(level="warning")  # 添加带参数的装饰器 log3()
def func3(n):
    print("from func3(), n is %d!" % (n), flush=True)


func3(0)

"""
以上语句相当于执行了如下操作：

func3 = log3('warning')(func3)
func3()

"""

print("-------------------- 类方法装饰器 --------------------")

"""
类方法的函数装饰器和函数的函数装饰器类似。
对于类方法来说，都有一个默认的形数 self，所以在装饰器的内部函数 wrapper 中也要传入该参数，其他的用法和函数装饰器相同。

类方法装饰如要需要传入参数，请参考含参装饰器，只要再封装一层即可。
"""


def decorator(func):
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        ret = func(self, *args, **kwargs)
        end_time = time.time()
        print("%s.%s() cost %f second!" % (self.__class__,
                                           func.__name__,
                                           end_time - start_time))
        return ret

    return wrapper


class TestDecorator(object):
    @decorator
    def mysleep(self, n):
        time.sleep(n)


obj = TestDecorator()
obj.mysleep(1)
