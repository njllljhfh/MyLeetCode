# -*- coding:utf-8 -*-
"""
闭包（closure）在 Python 中可以这样解释：
如果在一个内部函数中，对定义它的外部函数的作用域中的变量（甚至是外层之外，只要不是全局变量，也即内嵌函数中还可以嵌套定义内嵌函数）进行了引用，
那么这个子函数就被认为是闭包。
所以我们上面例子中的 inner() 函数就是一个闭包函数，简称为闭包。

inner() 函数 见文件 ---> 016_作用域和闭包_作用域链.py



闭包具有以下两个显著特点，可以认为闭包 = 内嵌函数 + 内嵌函数引用的变量环境：
    ● 它是函数内部定义的内嵌函数。
    ● 它引用了它作用域之外的变量，但非全局变量。
"""


# 如果我们将闭包作为外部函数的返回值，然后在外部调用这个闭包函数会怎样呢？
def offset(n):
    base = n

    def step(i):
        return base + i

    return step


offset0 = offset(0)
print(offset0.__code__.co_freevars)  # 自由变量
print(offset0.__closure__[0].cell_contents)
print("**********")
offset100 = offset(100)
print(offset100.__code__.co_freevars)
print(offset100.__closure__[0].cell_contents)
print("**********")

print(offset0(1))
print(offset100(1))

print(offset0.__code__.co_freevars[0], "=", offset0.__closure__[0].cell_contents)  # base还是能访问到
print(offset100.__code__.co_freevars[0], "=", offset100.__closure__[0].cell_contents)  # base还是能访问到

"""
按照常规分析，
第一次调用 offset(0) 时，base 的值是 0，
第二次调用 offset(100)后，base 的值应该变为 100，
但是执行结束后，base 作为局部变量应该被释放了，也即不能再被访问了，然而结果却并非如此。
"""

"""
实际上在 Python 中，当内嵌函数作为返回值传递给外部变量时，
将会把定义它时涉及到的引用环境和函数体自身复制后打包成一个整体返回，
这个整体就像一个封闭的包裹，不能再被打开修改，所以称为闭包很形象。
"""


# 对于上例中的 offset0 来说，
# 它的引用环境就是变量 base = 0 ，以及建立在引用环境上的函数体 `base + i` 。
# 引用 offset0() 和执行下面的函数是等价的:
def offset0(i):
    base = 0
    return base + i
