# -*- coding:utf-8 -*-
"""
即便执行了函数 foo()，local_var 实际上也分配过内存，执行依然报错，
所以 local_var 的作用域也只是在函数内部，函数结束时，局部变量所占的资源就被释放了，外部无法再访问。
"""


def foo():
    local_var = 0


foo()
print('local_var' in globals())
print(local_var)
