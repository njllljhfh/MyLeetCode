# -*- coding:utf-8 -*-
"""
所谓作用域的同名互斥性，是指在不同的两个作用域中，若定义了同名变量，
那么高优先级的作用域中不能同时访问这两个变量，只能访问其中之一。
"""

var = 0


# 报错：
#     global var
#     ^
# SyntaxError: name 'var' is used prior to global declaration
def foo():
    var = 1  # 定义了局部变量 var
    print(var)

    global var
    print(var)


"""
global 声明 var 是全局变量，也即 global 可以修改作用域链，当访问 var 变量时，直接跳转到全局作用域查找, 
错误提示在本语句前, 变量名 var 已经被占用了。
所以函数体内的局部作用域内，要么只使用 局部变量 var，要么在使用 var 前就声明是全局变量 var。
"""