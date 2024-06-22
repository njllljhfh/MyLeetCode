# -*- coding:utf-8 -*-
"""
Python 的作用域一共有4种，分别是：
    L （Locals）局部作用域，或作当前作用域。
    E （Enclosing）闭包函数外的函数中
    G （Globals）全局作用域
    B （Built-ins）内建作用域


Python 解释器查找变量时按照 L –> E –> G –>B 作用域顺序查找，
如果在局部作用域中找不到该变量，就会去局部的上一层的局部找（例如在闭包函数外的函数中），
还找不到就会去全局找，再者去内建作用域中查找。
"""


# 之前的示例已经涉及到前三种作用域，下面的示例对内建作用域进行验证。
def globals():
    return "from local globals()"


# 系统内建的函数 globals() 被我们自定义的同名函数“拦截”，
# 显然如果我们没有在全局作用域中定义此处的 globals()，则会去内建作用域中查找（将上面的globals定义注释，再执行试试看）。
print(globals())
