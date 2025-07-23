# -*- coding:utf-8 -*-
print("1 reduce()---------------------------------------------")


# reduce() 函数有两个参数，它把 function 计算结果结果继续和序列的下一个元素做累积计算。
# reduce() 的行为等价于：
def homo_reduce(func, seq):
    result = seq[0]
    for next in seq[1:]:
        result = func(result, next)
    return result


print("2 以下示例计算列表中所有数值的乘积---------------------------------------------")
# 以下示例计算列表中所有数值的乘积。
from functools import reduce

total = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(total)

initial = 10  # 初始值
total = reduce((lambda x, y: x * y), [1, 2, 3, 4], initial)
print(total)
