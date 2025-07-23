# -*- coding:utf-8 -*-
"""
函数名实际上就是一个变量，它指向了一个函数对象，所以可以有多个变量指向一个函数对象，并引用它。
"""


def foo():
    return abs


myabs = foo()
print(myabs(-1))

"""
以上示例直接把系统内建函数 abs() 作为返回值赋值给 myabs 变量，所以 myabs() 等价于 abs()。
"""
print("-----------------------------------------------------")

# 为了深入理解 Python 是如何处理函数作为返回值的，再看一个更复杂的例子。
flist = []
for i in range(3):
    def foo(x):
        print(x + i)


    flist.append(foo)

print(f"i = {i}")  # i == 2
for f in flist:
    f(1)

"""
按照预期，程序应该输出 1 2 3，然而却得到 3 3 3，这是因为以下两点：
    ● Python 中没有块作用域，当循环结束以后，循环体中的临时变量 i 作为全局变量不会销毁，它的值是 2。
    ● Python 在把函数作为返回值时，并不会把函数体中的全局变量替换为实际的值，而是原封不动的保留该变量。
"""


# flist 列表中的函数等价于如下的函数实现：
def flist_foo(x):
    global i
    print(x + i)


print("-----------------------------------------------------")
# 如果我们想要得到预期的效果，那么就要让全局变量变成函数内部的局部变量，把 i 作为参数传递给函数可以完成这一转换。
flist = []
for i in range(3):
    def foo(x, y=i):
        print(x + y)


    flist.append(foo)

for f in flist:
    f(1)
