# -*- coding:utf-8 -*-
"""
在代码块中定义的变量，它的作用域通常只在代码块中，这里测试下 Python 是否支持块作用域。
"""

dict0 = globals()
print(len(dict0))
print(dict0.keys())

# 块作用域（块作用域是不存在）
while True:  # 在代码块中定义 block_var
    block_var = "012345"
    break

print(block_var)
dict0 = globals()
print(len(dict0))
print(dict0.keys())

"""
从示例中，可以看出在 Python 中，在代码块结束后依然可以访问块中定义的变量，块作用域是不存在。
代码块中的定义的变量的作用域就是代码块所在的作用域。默认就是全局作用域。
在 globals() 的返回值中可以看到在代码块执行后，全局变量中出现了 block_var，为简便起见，这里只打印了全部变量名。
"""
